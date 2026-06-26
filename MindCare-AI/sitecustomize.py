"""Project-wide Python startup tweaks for local Windows terminals."""

import sys


for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")
