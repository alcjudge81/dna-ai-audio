"""Kokoro text-to-speech for lesson scripts. See PROJECT.md for model downloads."""
import re, os, json, hashlib, subprocess, time
import numpy as np, soundfile as sf
MODEL = os.environ.get("KOKORO_MODEL", "/home/claude/tts/models/kokoro-v1.0.fp16.onnx")
VOICES = os.environ.get("KOKORO_VOICES", "/home/claude/tts/models/voices-v1.0.bin")
CACHE = os.environ.get("TTS_CACHE", "/home/claude/course/.ttscache")
HERE = os.path.dirname(os.path.abspath(__file__))
SR = 24000
VMAP = {"A": "af_heart", "B": "am_michael"}
_k = None
def kokoro():
    global _k
    if _k is None:
        from kokoro_onnx import Kokoro
        _k = Kokoro(MODEL, VOICES)
    return _k
def load_lexicon(path=None):
    path = path or os.path.join(HERE, "lexicon.tsv"); rules = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#") or "\t" not in line: continue
            pat, rep = line.split("\t")[:2]; rules.append((re.compile(pat), rep))
    return rules
def speakable(text, rules):
    text = text.replace("—", ", ").replace("–", " to ").replace("*", "").replace("×", " times ")
    for pat, rep in rules: text = pat.sub(rep, text)
    return re.sub(r"\s+", " ", text).strip()
def split_sentences(par):
    return [p.strip() for p in re.split(r'(?<=[.!?])["\')\]]*\s+(?=[A-Z0-9"\'(\[])', par.strip()) if p.strip()]
def group(sents, maxlen=330):
    out, cur = [], ""
    for s in sents:
        if cur and len(cur) + 1 + len(s) > maxlen: out.append(cur); cur = s
        else: cur = (cur + " " + s).strip()
    if cur: out.append(cur)
    return out
def parse(path):
    """Untagged paragraph = voice A. '[B] ...' = voice B for that paragraph only. '---' = long pause. '#' lines are not spoken."""
    title, items = None, []
    for par in re.split(r"\n\s*\n", open(path, encoding="utf-8").read()):
        lines = [l for l in par.strip().split("\n") if l.strip()]
        if not lines: continue
        if lines[0].startswith("#") and title is None: title = lines[0].lstrip("# ").strip()
        lines = [l for l in lines if not l.startswith("#")]
        if not lines: continue
        text = " ".join(l.strip() for l in lines)
        if text == "---": items.append(("pause", 1.1)); continue
        voice = "A"; m = re.match(r"^\[([AB])\]\s*", text)
        if m: voice = m.group(1); text = text[m.end():]
        items.append(("say", voice, text)); items.append(("pause", 0.55))
    return title, items
def render(script, out, album="DNA Computing Audio Course", track="", speed=1.0, bitrate="48k"):
    os.makedirs(CACHE, exist_ok=True); rules = load_lexicon(); title, items = parse(script)
    audio, words, synth, t0 = [], 0, 0.0, time.time()
    for it in items:
        if it[0] == "pause": audio.append(np.zeros(int(SR * it[1]), dtype=np.float32)); continue
        voice = VMAP[it[1]]
        for chunk in group(split_sentences(it[2])):
            spoken = speakable(chunk, rules); words += len(chunk.split())
            cp = f"{CACHE}/" + hashlib.sha1(f"{os.path.basename(MODEL)}|{voice}|{speed}|{spoken}".encode()).hexdigest() + ".npy"
            if os.path.exists(cp): s = np.load(cp)
            else:
                t1 = time.time(); s, _ = kokoro().create(spoken, voice=voice, speed=speed, lang="en-us"); synth += time.time() - t1
                s = np.asarray(s, dtype=np.float32); np.save(cp, s)
            audio.append(s); audio.append(np.zeros(int(SR * 0.14), dtype=np.float32))
    wav = np.concatenate(audio) if audio else np.zeros(SR, dtype=np.float32)
    tmpw, part = out + ".tmp.wav", out + ".part.mp3"; sf.write(tmpw, wav, SR, subtype="PCM_16")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", tmpw, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1",
           "-c:a", "libmp3lame", "-b:a", bitrate, "-metadata", f"title={title}", "-metadata", f"album={album}",
           "-metadata", "artist=DNA Computing Audio Course", "-metadata", "genre=Education"]
    if track: cmd += ["-metadata", f"track={track}"]
    subprocess.run(cmd + [part], check=True); os.remove(tmpw); os.replace(part, out)
    dur = len(wav) / SR
    info = {"title": title, "seconds": round(dur), "minutes": round(dur / 60, 1), "words": words, "bytes": os.path.getsize(out),
            "synth_seconds": round(synth), "wall_seconds": round(time.time() - t0)}
    json.dump(info, open(out[:-4] + ".json", "w")); return info
if __name__ == "__main__":
    import sys; print(json.dumps(render(sys.argv[1], sys.argv[2])))
