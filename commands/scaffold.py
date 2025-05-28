import os

def match(input):
    return "scaffold assistant" in input

def run(input):
    base_path = os.getcwd()

    folders = [
        "core",
        "interfaces",
    ]

    files = {
        "core/command_handler.py": "# Command handler logic\n",
        "interfaces/cli.py": "# CLI logic\n",
        "interfaces/gui.py": "# GUI logic\n",
        "voice_assistant.py": "# Voice logic\n",
        "local_llm.py": "# Local model integration\n",
        "gui_assistant.py": "# GUI startup\n",
        "README.md": "# GPT Assistant Project\n",
        ".env": "OPENAI_API_KEY=\n",
    }

    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    for file_path, content in files.items():
        with open(os.path.join(base_path, file_path), "w") as f:
            f.write(content)

    return f"📁 Project scaffolded with {len(folders)} folders and {len(files)} files."
