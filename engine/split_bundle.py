"""Split a bundle file into scripts/<id>.txt. Lessons are separated by lines of the form '=== 2.7 ==='."""
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
txt = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"(?m)^=== ([0-9]+\.[0-9]+) ===\s*$", txt)
for i in range(1, len(parts), 2):
    lid, body = parts[i], parts[i + 1].strip() + "\n"
    open(f"{ROOT}/scripts/{lid}.txt", "w", encoding="utf-8").write(body)
    w = len(re.sub(r"(?m)^#.*$", "", body).split())
    print(f"{lid}: {w} words, about {w/165:.1f} min, B turns {body.count('[B]')}")
