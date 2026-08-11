🔐 STEGANOX – Secure Steganography Tool

https://rahulprajapati-x.github.io/stegx/


STEGANOX is a GUI-based steganography tool built using Python that securely hides any file inside an image using LSB (Least Significant Bit) steganography combined with AES-256 encryption.
It is designed for educational and cybersecurity learning purposes.
✨ Features
🔒 AES-256 password-based encryption
🖼 Hide any type of file inside an image
🖥 Modern GUI built with PyQt6
🧲 Drag & Drop file support
🔓 Secure file extraction with password verification
💻 Works on Windows, Linux, and macOS
🛠 Technologies Used
Python 3
PyQt6 – GUI framework
stegano (LSB) – Image steganography
cryptography (Fernet) – AES-256 encryption
Pillow – Image handling
📦 Prerequisites
Make sure the following are installed:
Python 3.9 or above
pip (Python package manager)
Check Python version:
python --version


📥 Installation (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/rahulprajapati-x/steganox.git
cd steganox
OR download ZIP and extract it.

or you can use direct this tool 
https://rahulprajapati-x.github.io/stegx/

2️⃣ Create a Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate


3️⃣ Install Required Dependencies
pip install pyqt6 stegano cryptography pillow
▶️ Run the Application
python steganox.py
The STEGANOX GUI window will open.
🧪 How to Use
🔐 Encode (Hide a File)
Enter a password
Select or drag:
Cover image
Secret file
Click ENCODE
Output file generated:
encoded.png
🔓 Decode (Extract a File)
Enter the same password
Select or drag the encoded image
Click DECODE
Extracted file saved as:
extracted_file
⚠️ Important Notes
Use PNG images for best results
Incorrect password → decryption fails
Do not rename encoded image before decoding
Tool is for educational and ethical use only
❌ Common Errors & Fixes
Module not found
pip install <module-name>
GUI not opening (Linux)
sudo apt install python3-pyqt6
📁 Project Structure
STEGANOX/
│
├── steganox.py
├── README.md
├── requirements.txt
└── assets/ (optional)
