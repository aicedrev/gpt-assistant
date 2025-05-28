import os

def match(input):
    return "make folder" in input

def run(input):
    folder_name = input.split("make folder")[-1].strip() or "new_folder"
    os.makedirs(folder_name, exist_ok=True)
    return f"📁 Folder created: {folder_name}"
