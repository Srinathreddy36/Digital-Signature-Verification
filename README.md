# 🛡️ Digital Signature Verification Tool

This tool helps you securely **sign** a file and allows others to **verify** its authenticity using **RSA encryption** and **SHA-256 hashing**. It protects your files from tampering and ensures the file was really sent by you.

---

## 📌 What Does It Do?

- ✅ Confirms if a file is original and unchanged  
- 🔐 Uses public/private keys (RSA) for security  
- 🧾 Works with any file: PDF, TXT, DOCX, etc.  
- 🚫 Deletes file if tampered

---

## 🧰 What You Need

- Python installed on your system  
- Internet to clone this repo  
- Run it using **command prompt or terminal**

---

## 🧾 How to Use

### 🔽 1. Download the Project

Open a terminal or command prompt:

```bash
git clone https://github.com/Srinathreddy36/Digital-Signature-Verification.git
cd Digital-Signature-Verification
pip install cryptography
python sign_file.py
python verify_signature.py
Enter the path to the file you received: agreement.pdf
Enter the path to the signature file: signature.sig
Enter the path to the sender's public key: public.pem
✅ Signature is valid. The file is authentic and untampered.
❌ Signature verification failed: File has been tampered with or public key is invalid.
⚠️  The file has been deleted for security.

🙋 Who is this for?
Students learning digital security 🧑‍🎓

Developers sharing sensitive files 👩‍💻

Anyone who wants to be sure a file wasn’t altered 🔐
🧠 Behind the Scenes
Uses RSA (2048-bit) for encryption

Hashes the file using SHA-256

Verifies that the original file hasn’t been changed

---

Would you like me to:
- Save this `README.md` in your local project folder,  
- Commit & push it to GitHub for you?

Let me know 💪
