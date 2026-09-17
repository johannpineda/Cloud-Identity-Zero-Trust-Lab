#!/usr/bin/env python3
"""Generate a compact Markdown identity incident report from JSON."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    event = json.loads(args.input.read_text(encoding="utf-8"))
    required = ("incident_id", "title", "severity", "status", "identity", "detection", "response", "outcome")
    missing = [key for key in required if not event.get(key)]
    if missing:
        raise SystemExit(f"Missing required values: {', '.join(missing)}")
    report = f"""# {event['incident_id']} — {event['title']}

| Field | Value |
|---|---|
| Severity | {event['severity']} |
| Status | {event['status']} |
| Identity | `{event['identity']}` |

## Detection

{event['detection']}

## Response

{event['response']}

## Outcome

{event['outcome']}
"""
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(report)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
