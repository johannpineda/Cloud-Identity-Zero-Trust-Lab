#!/usr/bin/env python3
"""Summarize sanitized Entra sign-in CSV records."""
from __future__ import annotations
import argparse, csv
from collections import Counter
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    with args.csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = {"timestamp", "user", "application", "result", "risk", "conditional_access"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit(f"CSV must contain: {', '.join(sorted(required))}")
    print(f"Records: {len(rows)}")
    for label, key in (("Results", "result"), ("Risk", "risk"), ("Conditional Access", "conditional_access")):
        values = Counter(row[key] for row in rows)
        print(f"{label}: " + ", ".join(f"{k}={v}" for k, v in sorted(values.items())))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
