import subprocess

def match(input):
    return "check disk" in input

def run(input):
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    return result.stdout
