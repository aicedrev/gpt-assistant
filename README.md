# 🤖 GPT Assistant

A modular command-line AI assistant built for productivity, automation, and local control.

## 🚀 Features

- 🖥️ Local CLI assistant with natural language input
- 📁 File/folder creation by prompt (`make folder X`)
- 🧠 Smart project scaffolding (`scaffold assistant`)
- 🧰 Git integration (`push to github with repo name X`)
- 📄 Chat logging (`chat_log.txt`)
- 🔐 SSH automation-ready
- 🧏‍♂️ Voice and GUI expansions coming soon
- 🔁 Designed for plug-and-play command modules

## 📦 Requirements

- Python 3.10+
- OpenAI Python SDK (`pip install openai`)
- python-dotenv (`pip install python-dotenv`)
- Git + SSH key connected to GitHub

## 🧠 Usage

\`\`\`bash
python assistant.py
\`\`\`

Then try:

- `make folder notes`
- `create file ideas.txt`
- `push to github with repo name gpt-assistant`

## 📂 Directory Structure

\`\`\`
gpt_assistant/
├── assistant.py
├── chat_log.txt
├── requirements.txt
├── core/
│   └── command_handler.py
├── gui_assistant.py
├── local_llm.py
├── voice_assistant.py
\`\`\`

## 🔭 Roadmap

- [ ] Streamlit GUI
- [ ] Voice interaction
- [ ] Hybrid GPT fallback
- [ ] Plugin registry

## 🛡 License

MIT

## 🤝 Contribute

PRs welcome. Modular design. Expand it!

