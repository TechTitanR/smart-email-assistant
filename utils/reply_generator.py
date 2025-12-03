# Template-based reply generator
import textwrap


def generate_reply(summary, tasks, meetings):
    lines = []
    lines.append("Hi,")
    lines.append("")
    if summary:
        lines.append("Thanks for the update. In brief:")
        lines.append(textwrap.fill(summary, width=80))
        lines.append("")
    if tasks:
        lines.append("I will work on the following items:")
        for i, t in enumerate(tasks, 1):
            lines.append(f"{i}. {t}")
        lines.append("")
    if meetings:
        lines.append("Regarding scheduling, I see the following mentions:")
        for m in meetings:
            lines.append(f"- {m}")
        lines.append("")
    lines.append(
        "Please let me know if I should prioritize any specific item or if there are any deadlines."
    )
    lines.append("Thanks,")
    lines.append("Rishi")
    return "\n".join(lines)
