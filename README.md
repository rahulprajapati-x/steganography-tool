🛠 STEGANOX – Installation & Setup Guide
This guide explains how to install and run STEGANOX (GUI-based Steganography Tool) on any system.
✅ 1. Prerequisites
Before installing the tool, make sure your system has:
✔️ Python 3.9 or above
✔️ Internet connection (only for first-time installation)
✔️ Windows / Linux / macOS
✅ 2. Check Python Installation
Open Terminal / Command Prompt and run:
python --version
or
python3 --version
If Python is not installed, download it from:
👉 https://www.python.org/downloads/
⚠️ IMPORTANT (Windows users)
While installing Python, check this option:
☑ Add Python to PATH
✅ 3. Download the Project
Option A: Using Git (Recommended)
git clone https://github.com/your-username/steganography-tool.git
cd steganography-tool
Option B: Manual Download
Click Code → Download ZIP
Extract the ZIP file
Open the extracted folder
✅ 4. Create a Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
You should see (venv) in your terminal.
✅ 5. Install Required Libraries
Run this command:
pip install pyqt6 stegano cryptography pillow
📌 These libraries are used for:
PyQt6 → GUI Interface
stegano → Image steganography (LSB)
cryptography → AES-256 encryption
pillow → Image processing
✅ 6. Run the Application
Make sure you are in the project folder and run:
python steganox.py
(or whatever your main file name is)
🎉 The GUI window will open!
✅ 7. How to Use the Tool
🔐 Encoding (Hide a File)
Enter a password
Drop or select:
A cover image
A secret file
Click ENCODE
Output file: encoded.png
🔓 Decoding (Extract a File)
Enter the same password
Drop or select the encoded image
Click DECODE
Extracted file saved as extracted_file
⚠️ Important Notes
Use PNG images for best results
Wrong password = decryption will fail
Tool is for educational & ethical use only
❌ Common Errors & Fixes
Error: ModuleNotFoundError
pip install missing_module_name
Error: GUI not opening (Linux)
sudo apt install python3-pyqt6
🚀 Optional (Advanced)
To create a .exe (Windows):
pip install pyinstaller
pyinstaller --onefile --windowed steganox.py
