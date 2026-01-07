import sys, base64, hashlib
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout,
    QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from stegano import lsb
from cryptography.fernet import Fernet

# ---------- Crypto ----------
def make_key(password):
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode()).digest()
    )

def encrypt(data, password):
    return Fernet(make_key(password)).encrypt(data)

def decrypt(data, password):
    return Fernet(make_key(password)).decrypt(data)

# ---------- Drag Label ----------
class DropBox(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.file_path = None
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedHeight(70)
        self.setStyleSheet("""
            QLabel {
                border: 2px dashed #22d3ee;
                color: #94a3b8;
                background-color: #020617;
            }
        """)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()

    def dropEvent(self, e):
        self.file_path = e.mimeData().urls()[0].toLocalFile()
        self.setText(self.file_path)

# ---------- Main App ----------
class SteganoX(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STEganoX | Hacker Steganography Tool")
        self.setFixedSize(900, 450)
        self.setStyleSheet("background:#020617; color:#e5e7eb;")

        title = QLabel("STEGANOX :: CYBER INTERFACE")
        title.setFont(QFont("Courier", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color:#22d3ee")

        self.key = QLineEdit()
        self.key.setPlaceholderText("Enter Password (AES-256)")
        self.key.setEchoMode(QLineEdit.EchoMode.Password)
        self.key.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #22d3ee;
                background:#020617;
                color:#22d3ee;
            }
        """)

        # Encode widgets
        self.img_box = DropBox("Drop IMAGE here")
        self.secret_box = DropBox("Drop SECRET FILE here")

        img_btn = QPushButton("Select Image")
        sec_btn = QPushButton("Select Secret File")

        img_btn.clicked.connect(self.pick_image)
        sec_btn.clicked.connect(self.pick_secret)

        # Decode widgets
        self.decode_box = DropBox("Drop ENCODED IMAGE here")
        dec_btn = QPushButton("Select Encoded Image")
        dec_btn.clicked.connect(self.pick_encoded)

        # Action buttons
        encode_btn = QPushButton("ENCODE (HIDE FILE)")
        decode_btn = QPushButton("DECODE (EXTRACT FILE)")

        encode_btn.setStyleSheet("background:#22c55e; font-size:16px;")
        decode_btn.setStyleSheet("background:#ef4444; font-size:16px; color:white;")

        encode_btn.clicked.connect(self.encode)
        decode_btn.clicked.connect(self.decode)

        # Layouts
        left = QVBoxLayout()
        left.addWidget(QLabel("ENCODE AREA"))
        left.addWidget(self.img_box)
        left.addWidget(img_btn)
        left.addWidget(self.secret_box)
        left.addWidget(sec_btn)
        left.addWidget(encode_btn)

        right = QVBoxLayout()
        right.addWidget(QLabel("DECODE AREA"))
        right.addWidget(self.decode_box)
        right.addWidget(dec_btn)
        right.addWidget(decode_btn)

        main = QVBoxLayout()
        main.addWidget(title)
        main.addWidget(self.key)
        main.addSpacing(10)
        main.addLayout(QHBoxLayout())
        h = QHBoxLayout()
        h.addLayout(left)
        h.addLayout(right)
        main.addLayout(h)

        self.setLayout(main)

    # ---------- File Pickers ----------
    def pick_image(self):
        p,_ = QFileDialog.getOpenFileName(self,"Select Image")
        if p:
            self.img_box.file_path = p
            self.img_box.setText(p)

    def pick_secret(self):
        p,_ = QFileDialog.getOpenFileName(self,"Select Secret File")
        if p:
            self.secret_box.file_path = p
            self.secret_box.setText(p)

    def pick_encoded(self):
        p,_ = QFileDialog.getOpenFileName(self,"Select Encoded Image")
        if p:
            self.decode_box.file_path = p
            self.decode_box.setText(p)

    # ---------- Encode ----------
    def encode(self):
        if not self.img_box.file_path or not self.secret_box.file_path:
            QMessageBox.warning(self,"Error","Select image and secret file")
            return
        if not self.key.text():
            QMessageBox.warning(self,"Error","Enter password")
            return

        with open(self.secret_box.file_path,"rb") as f:
            encrypted = encrypt(f.read(), self.key.text())

        img = lsb.hide(self.img_box.file_path, encrypted.decode("latin1"))
        img.save("encoded.png")

        QMessageBox.information(self,"Success","File hidden as encoded.png")

    # ---------- Decode ----------
    def decode(self):
        if not self.decode_box.file_path:
            QMessageBox.warning(self,"Error","Select encoded image")
            return
        if not self.key.text():
            QMessageBox.warning(self,"Error","Enter password")
            return

        try:
            hidden = lsb.reveal(self.decode_box.file_path)
            data = decrypt(hidden.encode("latin1"), self.key.text())
            with open("extracted_file","wb") as f:
                f.write(data)
            QMessageBox.information(self,"Success","File extracted")
        except:
            QMessageBox.critical(self,"Failed","Wrong password or invalid image")

# ---------- Run ----------
app = QApplication(sys.argv)
w = SteganoX()
w.show()
sys.exit(app.exec())
