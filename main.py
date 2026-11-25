"""Fortune Cookie for the Liquidated Trader.

One fortune-cookie line for a crypto trader who just got liquidated:
oracular opening, then the punchline breaks the fortune voice.
"""
import os

ENTRY = "The stars foretell great wealth in your future \u2014 they never said it would survive your liquidation."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
entry_path = os.path.join(output_dir, "entry.txt")
# Single line, no trailing newline: the entry is exactly the fortune.
with open(entry_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
