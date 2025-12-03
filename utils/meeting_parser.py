# Very simple meeting/date/time parser using regex (heuristic)
import re

MONTHS = (
    "(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|"
    "january|february|march|april|may|june|july|august|"
    "september|october|november|december)"
)
TIME_RE = r"(\b[0-2]?\d[:.][0-5]\d\b(?:\s?(?:am|pm))?)"
DATE_RE1 = r"(\b\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?\b)"
DATE_RE2 = r"(\b\d{1,2}\s+" + MONTHS + r"(?:\s+\d{2,4})?\b)"
RELATIVE = r"\b(today|tomorrow|next week|next month|this week|this month)\b"
WEEKDAY = r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b"


def parse_meetings(text):
    text_lower = text.lower()
    results = []
    # find times
    for m in re.findall(TIME_RE, text_lower):
        results.append(m[0] if isinstance(m, tuple) else m)
    # find explicit dates
    for m in re.findall(DATE_RE1, text_lower):
        results.append(m)
    for m in re.findall(DATE_RE2, text_lower):
        results.append(m)
    # relative mentions
    for m in re.findall(RELATIVE, text_lower):
        results.append(m)
    # weekdays
    for m in re.findall(WEEKDAY, text_lower):
        results.append(m)
    # dedupe and return
    final = []
    for r in results:
        if r not in final:
            final.append(r)
    return final
