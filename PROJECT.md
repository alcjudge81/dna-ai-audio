# DNA Computing Audio Course: project runbook

A personal audio curriculum for Alex (chemical engineering PhD student, Keung lab, NC State) on computing, analog versus digital
machines, how AI models are built, and molecular computing. This repository is the durable home of everything. It is public, so
nothing about Alex's own unpublished research ideas goes in it.

## What is where

| Path | What |
|---|---|
| `engine/syllabus_data.py` | The syllabus: every item, in order, Core or Depth, with lead-in text, links and NotebookLM prompts. Edit here. |
| `engine/briefs_data.py` | `STYLE` (rules for writing lesson scripts) and a brief for every custom lesson and desk lab. |
| `briefs.md`, `data/syllabus.json` | Generated copies of the two files above. |
| `scripts/<id>.txt` | Lesson scripts, written for the ear. The script is the master copy; audio is a render of it. |
| `audio/<id>.mp3` + `.json` | Rendered audio and its duration sidecar. |
| `feed.xml`, `index.html`, `cover.jpg` | The podcast feed and public page served by GitHub Pages from `main`. |
| `site/index.html` | The private course hub (a claude.ai artifact). `data/hub.json` holds its slug. |
| `engine/*.py` | `tts_lib.py`, `render_queue.py`, `build_hub.py`, `build_feed.py`, `split_bundle.py`, `make_cover.py`, `smoke.py`. |

Feed address: `https://alcjudge81.github.io/dna-ai-audio/feed.xml` (Apple Podcasts: Library, the three-dot menu, Follow a Show by URL).

## Set up a fresh session

```
pip install kokoro-onnx soundfile --break-system-packages
mkdir -p /home/claude/tts/models && cd /home/claude/tts/models
for f in kokoro-v1.0.fp16.onnx voices-v1.0.bin; do curl -sSL -o $f https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f; done
```
Voices: A = `af_heart` (narrator), B = `am_michael` (short questions only). Rendering runs at about 1.75x real time on two cores.

## The loop

1. Write or edit `scripts/<id>.txt` following `STYLE`.
2. Render: `nohup python3 engine/render_queue.py > /dev/null 2>&1 &` (renders every script without an up-to-date MP3, in order;
   resumable; a `.failed` file marks a script that crashed). A long render needs the session kept alive with foreground waits.
3. `python3 engine/build_feed.py && python3 engine/build_hub.py`
4. Commit and push `main` (Pages redeploys in a minute or two).
5. Republish the hub: `site/publish_files.json` lists the files for the artifact publish tool (patch mode, slug in `data/hub.json`).

## State on 16 November 2026

Done: syllabus (146 items), briefs for all 50 lessons and 7 desk labs, the tools above, the hub, and 21 lesson scripts (every keystone).
Scripts written so far are whatever is in `scripts/`. Everything else below is open.

## Remaining work, in order

1. **Render** all scripts in `scripts/`, rebuild feed and hub, push, republish the hub.
2. **Write the remaining lesson scripts** from their briefs (any lesson id in `briefs_data.py` with no file in `scripts/`).
   Read `STYLE`, the brief, and the two neighbouring scripts first. Facts marked CHECKED in briefs were verified against the papers.
   Do not add figures that are not in the brief unless you verify them.
3. **Lead-ins**: for every item that is not a lesson or a lab, write `scripts/<id>.txt` of 60 to 120 words: say what it is and who made
   it, then the item's `why` text, then where the link is ('in this episode's notes and in the course hub'). For papers add the
   NotebookLM setting. Render them; `build_feed.py` already puts links in the episode notes.
4. **Direct links**: items whose link has `check == "search"` (1.13, 2.13, 2.14, 3.19, 3.24, 3.26, 3.27, 3.28, 5.37, 5.57) and
   1.12 (no link) need a verified direct link. Verify by opening the page; never add a link from memory.
5. **Desk labs**: turn each lab brief into a ready-to-paste prompt for Claude Code plus a starter notebook under `labs/`.
6. **Depth to consider adding** (verify first): one or two audio-native episodes on analog in-memory or neuromorphic chips for
   Phase 2; recorded talks by Lulu Qian, Erik Winfree and David Soloveichik for Phase 5.
7. **Listen-check**: Alex reports mispronounced names; fix in `engine/lexicon.tsv` and re-render those lessons (the cache makes it cheap).

## Rules

- Every external link must be verified before it goes in the syllabus; record how in the link's `check` field.
- Paper records and DOIs came from PubMed; keep DOI links when citing them.
- Commit messages end with the session attribution lines in use at the time.
