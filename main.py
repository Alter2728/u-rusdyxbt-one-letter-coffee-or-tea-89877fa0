"""One Letter: Coffee or Tea — pick coffee."""

import os

# Revised pick: A for coffee. Coffee is the bolder, more vivid choice —
# dark, bitter, and jolting awake, the jolt that starts the day.
# Tea is gentle and quiet; coffee is the one that grabs you.
LETTER = "A"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w") as f:
    f.write(LETTER)
