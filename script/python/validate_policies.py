#!/usr/bin/env python3
"""Validate sanitized Conditional Access policy files."""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED = {"id", "displayName", "state", "cloudApps", "grantControls"}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("policy_directory", type=Path)
    args = parser.parse_args()
    files = sorted(args.policy_directory.glob("*.json"))
    if not files:
        print("FAIL: no policy JSON files found")
        return 1
    failures = 0
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            missing = REQUIRED - data.keys()
            controls = data.get("grantControls", {}).get("builtInControls", [])
            if missing or data.get("state") not in {"enabled", "disabled", "enabledForReportingButNotEnforced"} or not controls:
                raise ValueError(f"missing={sorted(missing)}, grantControls={controls}")
            print(f"PASS {path.name}: {data['displayName']}")
        except (json.JSONDecodeError, ValueError) as exc:
            failures += 1
            print(f"FAIL {path.name}: {exc}")
    print(f"Validated {len(files)} policies; failures={failures}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
