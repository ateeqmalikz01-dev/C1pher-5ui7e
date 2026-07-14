# C1pher-5ui7e
This project simulates the role of a Cybersecurity Analyst tasked with building a basic encryption/decryption tool. Rather than "cracking codes," the focus is on understanding how data confidentiality is achieved through mathematical and programmatic logic — protecting information in transit using a reversible, symmetric shift cipher.



# How to use(Linux Only)

clone the repo:
gh repo clone ateeqmalikz01-dev/C1pher-5ui7e

# Run

python3 cypher_tool.py

# 🔐 Basic Encryption & Decryption — Caesar Cipher

**Project 2 | DecodeLabs Industrial Training Kit | Batch 2026**

A simple yet foundational cryptography project that implements the classic **Caesar Cipher** algorithm to demonstrate core principles of data confidentiality — encrypting plaintext into ciphertext and reliably decrypting it back.

## 📌 Overview

This project simulates the role of a Cybersecurity Analyst tasked with building a basic encryption/decryption tool. Rather than "cracking codes," the focus is on understanding how data confidentiality is achieved through **mathematical and programmatic logic** — protecting information in transit using a reversible, symmetric shift cipher.

## 🎯 Objective

Implement a simple encryption and decryption technique that:
- Encrypts user-provided text using a Caesar Cipher (or similar substitution logic)
- Decrypts the encrypted text back to its original form
- Displays both the encrypted and decrypted output

## ⚙️ How It Works

The Caesar Cipher shifts each letter of the alphabet by a fixed number of positions (the **key**), using ASCII values and modular arithmetic to wrap around the 26-letter alphabet.

**Encryption formula:**
```
E(x) = (x + n) mod 26
```

**Decryption formula (reverse shift):**
```
D(x) = (x - n) mod 26
```

Where `x` is the character's alphabetical position and `n` is the shift key. Since the same key both encrypts and decrypts, this is a **symmetric encryption** scheme.

**Example:** With shift `n = 3`, the letter `A` (ASCII 65) becomes `D` (ASCII 68).

## 🧩 Features

- ✅ Encrypts plaintext into ciphertext using a configurable shift key
- ✅ Decrypts ciphertext back to the original plaintext
- ✅ Handles edge cases (spaces, punctuation, uppercase & lowercase letters)
- ✅ Displays both encrypted and decrypted output for verification
- ✅ Custom shift key support (stretch goal)
- ✅ Optional Vigenère cipher variant (stretch goal)

## 🛠️ Tech Stack

- Language: Python *(or update to your implementation language)*
- Core concepts: ASCII conversion (`ord()` / `chr()`), modular arithmetic, string manipulation

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Run the script
python caesar_cipher.py
```

## 📖 Usage

1. Enter the text you want to encrypt
2. Enter a shift key (integer)
3. View the generated ciphertext
4. The program automatically decrypts it back to verify correctness

## ⚠️ Known Limitations

The Caesar Cipher is intentionally basic and **not secure** for real-world use:
- **Tiny key space** — only 25 possible shifts, making brute-force attacks instantaneous
- **Pattern preservation** — letter frequency distribution in the ciphertext mirrors natural language, making it vulnerable to frequency analysis

This project serves as a foundation for understanding cryptographic concepts before progressing to modern, secure algorithms like **AES-256**.

## 🎓 Key Skills Demonstrated

- Encryption/decryption fundamentals
- Logic building & algorithmic thinking
- Data protection basics
- ASCII/character manipulation

## 📈 Roadmap / Future Improvements

- [ ] Implement Vigenère cipher for polyalphabetic substitution
- [ ] Add a GUI or web interface
- [ ] Add frequency analysis tool to demonstrate the cipher's vulnerability
- [ ] Extend to modern encryption standards (AES)

## 👤 Author
Ateeq ur Rehman as intern at **DecodeLabs.tech — Batch 2026**

---

*This project is for educational purposes, demonstrating foundational cryptography concepts as part of a cybersecurity training curriculum.*

