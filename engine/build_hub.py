"""Build site/index.html (the hub), data/syllabus.json and briefs.md from the syllabus and whatever scripts and audio exist."""
import json, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
from syllabus_data import PHASES, NLM_PREAMBLE
from briefs_data import BRIEFS, STYLE
stats = {"lessons": 0, "scripts": 0, "audio": 0}
for ph in PHASES:
    for it in ph["items"]:
        if it["kind"] != "lesson": continue
        stats["lessons"] += 1
        it["script"] = os.path.exists(f"{ROOT}/scripts/{it['id']}.txt"); stats["scripts"] += it["script"]
        side = f"{ROOT}/audio/{it['id']}.json"
        it["audio"] = os.path.exists(f"{ROOT}/audio/{it['id']}.mp3") and os.path.exists(side); stats["audio"] += it["audio"]
        if it["audio"]: it["mins"] = max(1, round(json.load(open(side))["seconds"] / 60))
data = {"updated": datetime.date.today().isoformat(), "preamble": NLM_PREAMBLE, "phases": PHASES}
json.dump(data, open(f"{ROOT}/data/syllabus.json", "w"), indent=1, ensure_ascii=False)
tpl = open(f"{HERE}/index.template.html", encoding="utf-8").read()
open(f"{ROOT}/site/index.html", "w", encoding="utf-8").write(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
with open(f"{ROOT}/briefs.md", "w", encoding="utf-8") as f:
    f.write("# Lesson briefs\n\n```\n" + STYLE.strip() + "\n```\n")
    for ph in PHASES:
        f.write(f"\n## Phase {ph['n']}: {ph['title']}\n")
        for it in ph["items"]:
            if it["id"] in BRIEFS: f.write(f"\n### {it['id']} {it['title']} ({it['track']}, about {it['mins']} min)\n\n{BRIEFS[it['id']]}\n")
files = [{"as": "index.html", "path": f"{ROOT}/site/index.html"}]
for ph in PHASES:
    for it in ph["items"]:
        if it.get("script"): files.append({"as": f"scripts/{it['id']}.txt", "path": f"{ROOT}/scripts/{it['id']}.txt"})
        if it.get("audio"): files.append({"as": f"audio/{it['id']}.mp3", "path": f"{ROOT}/audio/{it['id']}.mp3"})
json.dump(files, open(f"{ROOT}/site/publish_files.json", "w"))
print("hub built:", stats, "| files to publish:", len(files))
