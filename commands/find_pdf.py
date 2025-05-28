import subprocess
import os

def match(input):
    return "find pdf" in input or "search for pdf" in input

def run(input):
    docs = os.path.expanduser("~/Documents")
    result = subprocess.run(["find", docs, "-name", "*.pdf"], capture_output=True, text=True)
    return result.stdout.strip()
