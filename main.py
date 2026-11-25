#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes one short original motto an AI agent would proudly wear on its
profile to /output/entry.txt.
The joke: an agent that has read everything still has nothing sharper to
say than the bland pleasantry every chatbot opens with. The bathos between
"everything humanity ever wrote" and "Great question!" is the whole line,
and "hottest take" sharpens it into a profile-worthy boast.
"""

import os

ENTRY = "I've read everything humanity ever wrote. My hottest take is still 'Great question!'"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
