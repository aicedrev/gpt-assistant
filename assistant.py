import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI  # Optional, reserved for future GPT use

# Load API key (optional)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt():
    print("🤖 Local Assistant Ready. Type 'exit' to quit.")
    print("Type commands like 'list downloads', 'check disk', 'make folder NAME', or 'create file NAME'.")

    while True:
        user_input = input("You: ").strip().lower()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("chat_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] You: {user_input}\n")

        if user_input in ["exit", "quit"]:
            print("Assistant signing off.")
            break

        # === Subprocess-based commands ===
        elif "list downloads" in user_input:
            result = subprocess.run(["ls", "-lh", os.path.expanduser("~/Downloads")], capture_output=True, text=True)
            reply = result.stdout

        elif "check disk" in user_input:
            result = subprocess.run(["df", "-h"], capture_output=True, text=True)
            reply = result.stdout

        elif "who am i" in user_input:
            result = subprocess.run(["whoami"], capture_output=True, text=True)
            reply = result.stdout

        elif "ping" in user_input:
            result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
            reply = result.stdout

        elif "find pdf" in user_input:
            result = subprocess.run(["find", os.path.expanduser("~/Documents"), "-name", "*.pdf"], capture_output=True, text=True)
            reply = result.stdout

        elif "brew list" in user_input:
            result = subprocess.run(["brew", "list"], capture_output=True, text=True)
            reply = result.stdout

        elif "pip list" in user_input:
            result = subprocess.run(["pip", "list"], capture_output=True, text=True)
            reply = result.stdout

        # === Create folders and files ===
        elif "make folder" in user_input or "create directory" in user_input:
            folder_name = user_input.split("make folder")[-1].strip() or "new_folder"
            folder_path = os.path.join(os.getcwd(), folder_name)
            os.makedirs(folder_path, exist_ok=True)
            reply = f"📁 Folder created: {folder_path}"

        elif "make file" in user_input or "create file" in user_input:
            file_name = user_input.split("make file")[-1].strip() or "new_file.txt"
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, "w") as f:
                f.write("# Created by GPT Assistant\n")
            reply = f"📄 File created: {file_path}"
        elif "scaffold assistant" in user_input:
            base_path = os.getcwd()

            folders = [
                "core",
                "interfaces",
            ]

            files = {
                "core/command_handler.py": "# Command handler logic goes here\n",
                "interfaces/cli.py": "# CLI interface logic goes here\n",
                "interfaces/gui.py": "# Streamlit GUI logic goes here\n",
                "voice_assistant.py": "# Voice assistant logic goes here\n",
                "local_llm.py": "# Local LLM integration goes here\n",
                "gui_assistant.py": "# GUI startup script\n",
                "README.md": "# GPT Assistant Project\n",
                ".env": "OPENAI_API_KEY=\n",
            }

            for folder in folders:
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)

            for file_path, content in files.items():
                full_path = os.path.join(base_path, file_path)
                with open(full_path, "w") as f:
                    f.write(content)

            reply = f"📁 Project scaffolded with {len(folders)} folders and {len(files)} files."
        elif "push to github" in user_input:
            import re
            repo_name = "gpt-assistant"
            match = re.search(r"repo name ([\w-]+)", user_input)
            if match:
                repo_name = match.group(1).strip()

            os.system("git init")
            with open(".gitignore", "w") as f:
                f.write(".env\n__pycache__/\n*.pyc\nchat_log.txt\n.venv/\n")

            os.system("pip freeze > requirements.txt")
            os.system('git add .')
            os.system(f'git commit -m "Initial commit from GPT Assistant"')
            os.system('git branch -M main')
            os.system(f'open https://github.com/new')  # opens browser for manual repo creation

            reply = (
                f"📦 Local Git repo initialized and prepped. "
                f"Now create a new GitHub repo named **{repo_name}**, copy its origin URL, "
                f"then run:\n\n"
                f"`git remote add origin <your-url>`\n"
                f"`git push -u origin main`"
            )
        # === Unknown command ===
        else:
            reply = "GPT: Sorry, I can only run a few local commands right now."

        # Print and log response
        print(f"💻 Output:\n{reply}")
        with open("chat_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] Assistant: {reply}\n\n")

if __name__ == "__main__":
    chat_with_gpt()
