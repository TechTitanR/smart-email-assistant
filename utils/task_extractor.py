# Heuristic task extractor
import re

ACTION_KEYWORDS = [
    "please",
    "kindly",
    "could you",
    "can you",
    "please find",
    "please review",
    "please share",
    "please send",
    "please update",
    "let me know",
    "kindly share",
    "attach",
    "submit",
    "share",
    "send",
    "review",
    "update",
    "complete",
    "schedule",
    "confirm",
    "book",
    "arrange",
]


def extract_tasks(text):
    tasks = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if re.match(r"^(\-|\*|\d+\.)\s+", line):
            tasks.append(line.lstrip("-*0123456789. ").strip())
            continue
        low = line.lower()
        for kw in ACTION_KEYWORDS:
            if kw in low:
                idx = low.find(kw)
                candidate = line[idx:].strip()
                candidate = candidate.lstrip(",:;")
                if "," in candidate:
                    candidate = candidate.split(",")[0].strip()
                tasks.append(candidate.capitalize())
                break
    # remove duplicates while preserving order
    seen = set()
    final = []
    for t in tasks:
        if t not in seen:
            final.append(t)
            seen.add(t)
    return final
