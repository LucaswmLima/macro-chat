# Macro Chat

A lightweight Windows desktop application for creating, managing and executing chat macros quickly and efficiently.

Macro Chat was created to make repetitive chat messages easier to manage, allowing frequently used commands and messages to be triggered without having to type them manually every time.

## ✨ Features

* 📝 Create and manage custom chat macros
* ⚡ Quickly execute saved macros
* 🖥️ Simple Windows desktop interface
* 🎮 Designed with gaming and repetitive chat commands in mind
* 📦 Standalone Windows executable available through GitHub Releases

## 📥 Download

The latest version of Macro Chat can be downloaded from the **Releases** page:

**[⬇️ Download Macro Chat](https://github.com/LucaswmLima/macro-chat/releases/latest)**

### Windows

Download the latest `.exe` file from the release assets and run it.

No Python installation is required when using the compiled version.

## 🚀 Getting Started

### Using the executable

1. Download the latest `Macro Chat.exe` from Releases.
2. Run the executable.
3. Configure your macros.
4. Use the configured shortcuts/actions to send your messages.

### Running from source

If you want to run or modify the project from source, make sure you have Python installed.

Clone the repository:

```bash
git clone https://github.com/LucaswmLima/macro-chat.git
cd macro-chat
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the application:

```bash
python main.py
```

> The exact entry-point and dependency commands may vary depending on the current project structure.

## 🛠️ Building

Macro Chat can be packaged as a standalone Windows executable using PyInstaller.

Example:

```bash
pyinstaller --noconfirm --clean --onefile --windowed --name "Macro Chat" --icon="icon.ico" main.py
```

The generated executable will be placed inside the `dist` directory.

## 📁 Project Structure

```text
macro-chat/
├── main.py
├── icon.ico
├── requirements.txt
├── .gitignore
└── README.md
```

## 🎯 Use Cases

Macro Chat can be useful for:

* Frequently used gaming commands
* Repetitive chat messages
* Community/server commands
* Testing chat interactions
* Quickly accessing predefined messages
* Other workflows involving repetitive text input

## 🔒 Privacy

Macro Chat is designed to run locally on your Windows machine.

No account or external service is required to use the standalone application.

## 📄 License

This project is currently available for personal and educational use.

A formal open-source license may be added in the future.

## 👤 Author

**Lucas William**

GitHub: [@LucaswmLima](https://github.com/LucaswmLima)

---

⭐ If you find Macro Chat useful, consider giving the project a star!
