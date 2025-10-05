# Caesar Cipher 🔐
A simple yet powerful Python program that encrypts and decrypts messages using the **Caesar Cipher** algorithm.  
Developed by **Shahwan Alchomer**.

---

## 🚀 Features
- Encrypt text by shifting letters a set number of places
- Automatically decrypt messages using English letter frequency
- Supports both uppercase and lowercase
- Keeps punctuation and spaces unchanged
- Includes a CLI (Command Line Interface)

---

## 🧩 Example Usage

### 🔸 Import and use in Python
```python
from caesar_cipher import encipher, decipher

text = "Hello World"
cipher = encipher(text, 3)
print(cipher)         # Khoor Zruog
print(decipher(cipher))  # Hello World
