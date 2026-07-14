#!/usr/bin/env python3
"""
Mr A Tools — Caesar & Vigenère Cipher Suite
------------------------------------------------
Classic encryption/decryption tool with ASCII math.
"""

import os
import sys


# ──────────────────────────────────────────────
#  BANNER
# ──────────────────────────────────────────────

BANNER = r"""
███    ███ ██████       █████     ████████  ██████   ██████  ██      ███████
████  ████ ██   ██     ██   ██       ██    ██    ██ ██    ██ ██      ██
██ ████ ██ ██████      ███████       ██    ██    ██ ██    ██ ██      ███████
██  ██  ██ ██   ██     ██   ██       ██    ██    ██ ██    ██ ██           ██
██      ██ ██   ██     ██   ██       ██     ██████   ██████  ███████ ███████
"""

TOOL_TITLE = """
╔══════════════════════════════════════════════════╗
║          CAESAR & VIGENÈRE CIPHER SUITE          ║
╚══════════════════════════════════════════════════╝
"""


# ──────────────────────────────────────────────
#  CIPHER CORE
# ──────────────────────────────────────────────

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher: E(x) = (x + shift) % 26"""
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)  # spaces, punctuation, digits — pass through
    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar cipher: D(x) = (x - shift) % 26"""
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text: str, key: str) -> str:
    """Encrypt text using Vigenère cipher with repeating keyword."""
    if not key:
        return text
    key = key.upper()
    result = []
    key_index = 0
    for ch in text:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
            key_index += 1
        elif 'a' <= ch <= 'z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(text: str, key: str) -> str:
    """Decrypt text using Vigenère cipher with repeating keyword."""
    if not key:
        return text
    key = key.upper()
    result = []
    key_index = 0
    for ch in text:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            key_index += 1
        elif 'a' <= ch <= 'z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


# ──────────────────────────────────────────────
#  HELPER
# ──────────────────────────────────────────────

def read_shift(prompt: str) -> int:
    """Read an integer shift from stdin with retry."""
    while True:
        try:
            raw = input(prompt).strip()
            if raw == '':
                print("  [!] Shift cannot be empty.")
                continue
            val = int(raw)
            return val
        except ValueError:
            print("  [!] Please enter a valid integer.")


def read_key(prompt: str) -> str:
    """Read a non-empty alphabetic key for Vigenère."""
    while True:
        raw = input(prompt).strip()
        if raw == '':
            print("  [!] Key cannot be empty.")
            continue
        if not raw.replace(' ', '').isalpha():
            print("  [!] Key must contain only letters (A-Z, a-z).")
            continue
        return raw


# ──────────────────────────────────────────────
#  MENU
# ──────────────────────────────────────────────

MENU = """
  ┌───────────────────────────────────────────────┐
  │  1) Caesar Cipher — Encrypt                   │
  │  2) Caesar Cipher — Decrypt                   │
  │  3) Vigenère Cipher — Encrypt                 │
  │  4) Vigenère Cipher — Decrypt                 │
  │  5) Exit                                      │
  └───────────────────────────────────────────────┘
"""


def run_caesar(mode: str):
    """Interactive Caesar workflow."""
    print(f"\n  --- CAESAR CIPHER — {mode.upper()} ---\n")
    text = input("  Enter text: ")
    shift = read_shift("  Enter shift key (integer): ")

    if mode == 'encrypt':
        result = caesar_encrypt(text, shift)
        reverse = caesar_decrypt(result, shift)
        label = 'ENCRYPTED'
    else:
        result = caesar_decrypt(text, shift)
        reverse = caesar_encrypt(result, shift)
        label = 'DECRYPTED'

    print(f"\n  ═══════════════════════════════════════")
    print(f"  {label}: {result}")
    print(f"  ─────────────────────────────────────────")
    print(f"  Reverse check ({'dec' if mode == 'encrypt' else 'enc'}): {reverse}")
    print(f"  ═══════════════════════════════════════")
    input("\n  Press Enter to continue...")


def run_vigenere(mode: str):
    """Interactive Vigenère workflow."""
    print(f"\n  --- VIGENÈRE CIPHER — {mode.upper()} ---\n")
    text = input("  Enter plaintext: ")
    key = read_key("  Enter keyword (letters only): ")

    if mode == 'encrypt':
        result = vigenere_encrypt(text, key)
        reverse = vigenere_decrypt(result, key)
        label = 'CIPHERTEXT'
    else:
        result = vigenere_decrypt(text, key)
        reverse = vigenere_encrypt(result, key)
        label = 'PLAINTEXT'

    print(f"\n  ═══════════════════════════════════════")
    print(f"  {label}: {result}")
    print(f"  ─────────────────────────────────────────")
    print(f"  Reverse check ({'dec' if mode == 'encrypt' else 'enc'}): {reverse}")
    print(f"  ═══════════════════════════════════════")
    input("\n  Press Enter to continue...")


def main():
    """Main loop."""
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print banner
    print(BANNER)
    print(TOOL_TITLE)

    while True:
        print(MENU)
        choice = input("  Select option [1-5]: ").strip()

        if choice == '1':
            run_caesar('encrypt')
        elif choice == '2':
            run_caesar('decrypt')
        elif choice == '3':
            run_vigenere('encrypt')
        elif choice == '4':
            run_vigenere('decrypt')
        elif choice == '5':
            print("\n  Goodbye.\n")
            sys.exit(0)
        else:
            print("  [!] Invalid choice. Please enter 1-5.")
            continue

        # Re-clear for next iteration
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BANNER)
        print(TOOL_TITLE)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Interrupted. Goodbye.\n")
        sys.exit(0)

