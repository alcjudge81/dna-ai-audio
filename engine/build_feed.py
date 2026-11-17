"""Build feed.xml and the public index.html from rendered audio. Run after rendering, then commit and push."""
import json, os, sys, datetime
from email.utils import format_datetime
from xml.sax.saxutils import escape
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
from syllabus_data import PHASES
BASE = "https://alcjudge81.github.io/dna-ai-audio"
T0 = datetime.datetime(2026, 11, 16, 12, 0, tzinfo=datetime.timezone.utc)
eps, gi = [], 0
for ph in PHASES:
    n = 0
    for it in ph["items"]:
        gi += 1; n += 1
        mp3, side = f"{ROOT}/audio/{it['id']}.mp3", f"{ROOT}/audio/{it['id']}.json"
        if not (os.path.exists(mp3) and os.path.exists(side)): continue
        s = json.load(open(side))
        desc = it.get("sum") or it.get("why") or ""
        for l in it.get("links") or []: desc += f"\n{l['label']}: {l['url']}"
        eps.append({"id": it["id"], "title": f"{it['id']} {it['title']}", "desc": desc, "season": ph["n"] + 1, "ep": n, "secs": s["seconds"],
                    "bytes": os.path.getsize(mp3), "date": format_datetime(T0 + datetime.timedelta(minutes=gi)), "depth": it["track"] == "depth"})
x = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:content="http://purl.org/rss/1.0/modules/content/">', "<channel>",
     "<title>DNA Computing Audio Course</title>", f"<link>{BASE}/</link>", "<language>en-us</language>",
     "<description>A personal audio course on computing, analog and digital machines, how AI models are built, and molecular computing. Lessons are numbered in listening order.</description>",
     "<itunes:author>DNA Computing Audio Course</itunes:author>", "<itunes:type>serial</itunes:type>", "<itunes:explicit>false</itunes:explicit>",
     f'<itunes:image href="{BASE}/cover.jpg"/>', '<itunes:category text="Education"/>', "<itunes:block>Yes</itunes:block>"]
for e in eps:
    x += ["<item>", f"<title>{escape(e['title'])}</title>", f"<description>{escape(e['desc'])}</description>",
          f'<enclosure url="{BASE}/audio/{e["id"]}.mp3" length="{e["bytes"]}" type="audio/mpeg"/>',
          f'<guid isPermaLink="false">dna-ai-audio-{e["id"]}</guid>', f"<pubDate>{e['date']}</pubDate>",
          f"<itunes:duration>{e['secs']}</itunes:duration>", f"<itunes:season>{e['season']}</itunes:season>", f"<itunes:episode>{e['ep']}</itunes:episode>",
          "<itunes:episodeType>full</itunes:episodeType>", "</item>"]
x += ["</channel>", "</rss>"]
open(f"{ROOT}/feed.xml", "w", encoding="utf-8").write("\n".join(x) + "\n")
h = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>DNA Computing Audio Course</title>',
     "<style>body{font:17px/1.5 system-ui,sans-serif;max-width:640px;margin:0 auto;padding:24px 18px;color:#15202b;background:#f2f5f7}h1{font-size:28px;line-height:1.15}h2{font-size:17px;margin:22px 0 6px}audio{width:100%}code{word-break:break-all}p.m{color:#586675;font-size:15px}@media(prefers-color-scheme:dark){body{background:#0e141a;color:#e5ecf2}p.m{color:#9ba9b6}}</style></head><body>",
     "<h1>DNA Computing Audio Course</h1>", f"<p>Podcast feed address, for Follow a Show by URL in a podcast app:</p><p><code>{BASE}/feed.xml</code></p>",
     f"<p class='m'>{len(eps)} lessons rendered so far. Tap one to play it here.</p>"]
for e in eps: h += [f"<h2>{escape(e['title'])}</h2>", f'<audio controls preload="none" src="audio/{e["id"]}.mp3"></audio>']
h.append("</body></html>")
open(f"{ROOT}/index.html", "w", encoding="utf-8").write("\n".join(h) + "\n")
print("feed built:", len(eps), "episodes,", round(sum(e["secs"] for e in eps) / 60), "min")
