"""Render every script that has no up-to-date MP3, in syllabus order. Safe to start twice (lock file). Stop with a STOP_RENDER file."""
import os, sys, time, glob, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
LOCK = ROOT + "/.render.lock"
if os.path.exists(LOCK):
    try:
        os.kill(int(open(LOCK).read().strip()), 0); print("renderer already running"); sys.exit(0)
    except Exception: pass
open(LOCK, "w").write(str(os.getpid()))
import tts_lib
def key(p):
    try: a, b = os.path.basename(p)[:-4].split(".")[:2]; return (int(a), int(b))
    except Exception: return (99, 0)
def todo():
    out = []
    for p in sorted(glob.glob(ROOT + "/scripts/*.txt"), key=key):
        m = ROOT + "/audio/" + os.path.basename(p)[:-4] + ".mp3"
        if os.path.exists(p + ".failed"): continue
        if not os.path.exists(m) or os.path.getmtime(p) > os.path.getmtime(m): out.append((p, m))
    return out
idle, limit = 0, int(os.environ.get("IDLE_POLLS", "60"))
log = open(ROOT + "/render.log", "a")
while idle < limit and not os.path.exists(ROOT + "/STOP_RENDER"):
    t = todo()
    if not t: idle += 1; time.sleep(30); continue
    idle = 0; p, m = t[0]
    try:
        info = tts_lib.render(p, m, track=os.path.basename(p)[:-4]); log.write(json.dumps({"id": os.path.basename(p)[:-4], **info}) + "\n")
    except Exception as e:
        open(p + ".failed", "w").write(repr(e)); log.write(f"FAILED {p}: {e!r}\n")
    log.flush()
try: os.remove(LOCK)
except Exception: pass
