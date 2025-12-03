# Smart Email Assistant (Python Automation Project)

A lightweight, dependency-free Python automation tool that analyzes raw email text and produces:
- A short summary  
- A list of actionable tasks  
- Meeting/date/time detection  
- A clean, professional draft reply  

This project demonstrates **Python scripting, data parsing, automation logic, and modular pipeline design** — all without external ML libraries.

---

## 🚀 Features

### ✔ Email Summarization  
Extracts the most important sentences using a frequency-based algorithm.

### ✔ Task Extraction  
Uses keyword heuristics + regex to identify actionable items (e.g., *review, update, share, schedule…*).

### ✔ Meeting & Schedule Detection  
Captures dates, times, weekdays, and relative mentions like *tomorrow*, *next week*, etc.

### ✔ Draft Reply Generation  
Automatically creates a structured professional response based on extracted insights.

---

## 🗂 Folder Structure


## Structure
```
smart-email-assistant/
│
├── main.py # CLI entrypoint
├── utils/
│ ├── summarizer.py
│ ├── task_extractor.py
│ ├── meeting_parser.py
│ └── reply_generator.py
│
├── samples/
│ ├── email1.txt
│ └── email2.txt
│
├── tests/
│ └── test_run.py # Basic pytest for CLI testing
│
├── requirements.txt
├── .gitignore
├── .pre-commit-config.yaml
└── .github/workflows/python-app.yml
```
---

## 🧪 Example Usage
```bash
# from project root
python3 main.py --file samples/email1.txt
# or
python3 main.py --file samples/email2.txt
# or pass text directly
python main.py --text "Hi, can you update the report and schedule a meeting for Monday 3 PM?"

```
---

## Example output
===== SUMMARY =====
Please review the attached report and share updated numbers.

===== TASKS =====
1. Review the attached report
2. Share updated numbers
3. Schedule a call

===== MEETINGS =====
- tuesday
- 10:30 am

===== DRAFT REPLY =====
Hi,

Thanks for the update. In brief:
<summary>

I will work on the following items:
1. Review the attached report
2. Share updated numbers
3. Schedule a call

Regarding scheduling, I see the following mentions:
- Tuesday
- 10:30 am

Please let me know if I should prioritize anything specific.
Thanks,  
Rishi

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/YOUR_USERNAME/smart-email-assistant.git
cd smart-email-assistant
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## 🧩 Run Tests

```bash
pytest -q
```

---

## 🔄 GitHub Actions CI

- This repository includes a CI workflow that automatically runs:
- Black formatting check
- Flake8 linting
- Pytest on sample inputs

Located at:
```bash
.github/workflows/python-app.yml
```

---

## 🎯 Tool Demonstrated

- Clean, modular Python code
- Automation scripts for real-world workflows
- CLI tool development
- Data parsing, regex, text processing
- Baseline analytics logic
- CI pipelines & testing

---

## 📌 Future Improvements

- Smarter NLP with spaCy or transformers
- Better date/time normalization
- Web UI dashboard
- Export tasks to CSV or Notion
- Ability to process full email threads

---

## 👨‍💻 Author

- Rishi Bakliwal
- B.Tech IT, Manipal University Jaipur
- GitHub: [Rishi Bakliwal](https://github.com/TechTitanR/)

---
