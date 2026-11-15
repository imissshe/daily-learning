#!/usr/bin/env python3
"""把当天（UTC 日期）的贡献次数补到 TARGET 次。

只补差额：先数今天作者/提交者邮箱是用户本人的提交数，
不够 10 次就从题库里取小笔记，一篇笔记 = 一个提交，写进 extras/。
用户自己的学习内容（algorithms/、notes/、README 索引）一律不动。
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

TARGET = 10
AUTHOR_EMAIL = "84082201+imissshe@users.noreply.github.com"
REPO_ROOT = Path(__file__).resolve().parent.parent
EXTRAS_DIR = REPO_ROOT / "extras"
EPOCH = date(2026, 11, 15)


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout


def count_today(today: date) -> int:
    """数今天（UTC）作者或提交者是用户的提交数。"""
    start = f"{today.isoformat()}T00:00:00Z"
    end = f"{today.isoformat()}T23:59:59Z"
    out = git(
        "log",
        f"--since={start}",
        f"--until={end}",
        "--format=%ae %ce",
    )
    return sum(1 for line in out.splitlines() if AUTHOR_EMAIL in line)


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    today = date.today()
    count = count_today(today)
    missing = TARGET - count
    print(f"today={today} count={count} target={TARGET} missing={missing}")
    if missing <= 0:
        print("already at target, nothing to do")
        return 0

    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from topup_bank import BANK

    bank = BANK
    day_index = (today - EPOCH).days
    start = (day_index * TARGET) % len(bank)

    picked = []
    i = 0
    while len(picked) < missing and i < len(bank):
        entry = bank[(start + i) % len(bank)]
        i += 1
        path = EXTRAS_DIR / f"{today.isoformat()}-{entry['slug']}.md"
        if path.exists():
            continue
        picked.append((entry, path))

    if len(picked) < missing:
        print(f"warning: bank exhausted, only {len(picked)} notes available")
    for entry, path in picked:
        print(f"plan: {path.relative_to(REPO_ROOT)}")

    if dry_run:
        return 0

    EXTRAS_DIR.mkdir(exist_ok=True)
    for entry, path in picked:
        path.write_text(
            f"# {entry['title']}\n\n"
            f"> 补记 · {today.isoformat()}（每日贡献补齐）\n\n"
            f"{entry['body']}\n",
            encoding="utf-8",
        )
        subprocess.run(["git", "add", str(path)], cwd=REPO_ROOT, check=True)
        subprocess.run(
            ["git", "commit", "-m", f"extras: {entry['slug']} ({today.isoformat()})"],
            cwd=REPO_ROOT,
            check=True,
        )
        print(f"committed: {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
