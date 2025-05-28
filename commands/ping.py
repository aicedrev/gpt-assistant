
import subprocess

def match(input):
    return "ping" in input

def run(input):
    result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
    return result.stdout
