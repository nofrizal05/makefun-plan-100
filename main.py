"""Write the 30-day $100-to-profit plan to the make.fun output directory.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

PLAN = (
    "Day 1: list 3 fixed gigs on Contra + Upwork: AI receptionist for dental "
    "clinics, $149, 48h delivery. Days 2-30: build each with Twilio voice AI "
    "+ Calendly, deliver in 2 days, ask each client for 2 referrals. Spend "
    "$100 on Twilio credits + ads. Likely: 6 clients, ~$894 by day 30."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
