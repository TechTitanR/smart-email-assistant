# Smart Email Assistant (Lightweight)

A small, dependency-free Python utility that demonstrates email summarization, task extraction, meeting parsing, and draft reply generation. Designed as a resume-friendly project: pure Python, automation-focused, and easy to extend.

## Features
- Summarize long emails into 1-3 sentences using a frequency-based summarizer.
- Extract actionable tasks using heuristic rules and keywords.
- Detect simple meeting/date/time mentions using regex heuristics.
- Generate a polite draft reply combining summary, tasks, and scheduling notes.

## Structure
```
smart-email-assistant/
├── main.py                 # CLI entrypoint
├── utils/
│   ├── summarizer.py
│   ├── task_extractor.py
│   ├── meeting_parser.py
│   └── reply_generator.py
├── samples/
│   ├── email1.txt
│   └── email2.txt
└── README.md
```

## How to run
```bash
# from project root
python3 main.py --file samples/email1.txt
# or
python3 main.py --file samples/email2.txt
# or pass text directly
python3 main.py --text "Paste email content here..."
```

## Example output
Summary, extracted tasks, meeting mentions, and a draft reply will be printed to the console.

## Why this is resume-friendly
- Pure Python (no heavy ML libraries).
- Shows automation, data parsing, and pipeline orchestration.
- Easy to explain in interviews: focus on rules, heuristics, and modularity.

## Next steps / extensions (optional)
- Replace summarizer with an embedding-based method (use OpenAI or local models).
- Add named-entity recognition for more robust meeting parsing.
- Create a simple web UI or CLI flags to export CSV of tasks.
- Add unit tests and CI workflow for the repo.

---
Generated for Rishi Bakliwal (resume project).

## Push-ready GitHub Setup

This repository is ready to push to GitHub. It includes:
- `requirements.txt` (dev tools included)
- `black` and `flake8` for linting
- `pytest` for running basic tests
- GitHub Actions workflow to run lint + tests on push/pull_request

### How to push
```bash
git init
git add .
git commit -m "Initial: Smart Email Assistant - push-ready"
git branch -M main
# create a repo on GitHub, then:
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
```

### Run CI locally (example)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
black --check .
flake8
pytest -q
```

