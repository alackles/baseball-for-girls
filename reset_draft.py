"""
reset_draft.py
Resets draft state: clears draft_picks and rosters.
Teams, players, and draft queues are preserved.

Usage:
    python reset_draft.py
    DATABASE_PATH=test_draft.db python reset_draft.py
"""

import os
import sqlite3
import sys
from pathlib import Path

DB_PATH = os.environ.get("DATABASE_PATH", str(Path(__file__).parent / "fantasy.db"))


def reset_draft():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("BEGIN")
    conn.execute("DELETE FROM rosters")
    conn.execute("DELETE FROM draft_picks")
    conn.execute("COMMIT")
    conn.close()
    print(f"Draft reset complete. Database: {DB_PATH}")
    print("Teams, players, and draft queues are intact.")


if __name__ == "__main__":
    confirm = input(
        f"This will DELETE all picks and rosters from:\n  {DB_PATH}\nType 'yes' to continue: "
    )
    if confirm.strip().lower() == "yes":
        reset_draft()
    else:
        print("Aborted.")
