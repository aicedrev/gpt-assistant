import os
import subprocess

def match(input):
    return "list downloads" in input

def run(input):
    downloads_path = os.path.expanduser("~/Downloads")
    result = subprocess.run(["ls", "-lh", downloads_path], capture_output=True, text=True)
    return f"📂 Downloads Directory:\n{result.stdout}"
