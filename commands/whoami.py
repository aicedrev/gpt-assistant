import subprocess

def match(input):
    return "who am i" in input or "what user" in input

def run(input):
    result = subprocess.run(["whoami"], capture_output=True, text=True)
    return result.stdout.strip()
