import os
import re

def match(input):
    return "push to github" in input

def run(input):
    repo_name = "gpt-assistant"
    match = re.search(r"repo name ([\w\-]+)", input)
    if match:
        repo_name = match.group(1).strip()

    os.system("git init")
    with open(".gitignore", "w") as f:
        f.write(".env\n__pycache__/\nchat_log.txt\n.venv/\n")

    os.system("pip freeze > requirements.txt")
    os.system("git add .")
    os.system("git commit -m 'Initial commit from GPT Assistant'")
    os.system("git branch -M main")
    os.system("open https://github.com/new")  # opens browser to create repo manually

    return (
        f"📦 Local Git repo initialized.\n"
        f"🧠 Now create a new GitHub repo named **{repo_name}**, copy its origin URL, then run:\n\n"
        "```bash\n"
        f"git remote add origin https://github.com/YOUR_USER/{repo_name}.git\n"
        "git push -u origin main\n```"
    )
