#!/usr/bin/env python3
"""
Smart Email Assistant - simple, offline Python utility

Features:
- Summarize an email (extract top sentences)
- Extract actionable tasks (heuristic + regex)
- Parse simple meeting/date/time mentions
- Generate a polite draft reply using templates

Usage:
    python3 main.py --file samples/email1.txt
    python3 main.py --text "Paste email text here..."

This tool is intentionally lightweight and dependency-free.
"""
import argparse
import os

from utils.summarizer import summarize_text
from utils.task_extractor import extract_tasks
from utils.meeting_parser import parse_meetings
from utils.reply_generator import generate_reply


def read_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def run(text):
    summary = summarize_text(text, num_sentences=3)
    tasks = extract_tasks(text)
    meetings = parse_meetings(text)
    reply = generate_reply(summary, tasks, meetings)
    return dict(summary=summary, tasks=tasks, meetings=meetings, reply=reply)


def main():
    parser = argparse.ArgumentParser(
        description="Smart Email Assistant (simple offline)"
    )
    parser.add_argument("--file", "-f", help="Path to email text file")
    parser.add_argument("--text", "-t", help="Email text directly as argument")
    args = parser.parse_args()
    if args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            return 1
        text = read_file(args.file)
    elif args.text:
        text = args.text
    else:
        print(
            "Please provide --file or --text. Example: "
            "python3 main.py --file samples/email1.txt"
        )
        return 1

    out = run(text)
    print("\n===== SUMMARY =====\n")
    print(out["summary"])
    print("\n===== TASKS =====\n")
    if out["tasks"]:
        for i, t in enumerate(out["tasks"], 1):
            print(f"{i}. {t}")
    else:
        print("No explicit tasks detected.")
    print("\n===== MEETINGS =====\n")
    if out["meetings"]:
        for m in out["meetings"]:
            print(f"- {m}")
    else:
        print("No meeting/date/time mentions detected.")
    print("\n===== DRAFT REPLY =====\n")
    print(out["reply"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
