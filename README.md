# HybridCrypt

HybridCrypt is an educational cryptography project built entirely in Python. The project demonstrates the core concepts behind modern encryption systems by combining a custom symmetric cipher with RSA-based key exchange to create a hybrid encryption framework.

> Educational Project Only
>
> This project is designed for learning cryptography concepts and should not be used for protecting real-world sensitive data.

---

## Features

### Symmetric Encryption
- Multi-round encryption
- XOR-based key mixing
- Bit rotation operations
- S-Box substitution layer
- Permutation layer
- Diffusion mixing layer
- Key scheduling

### Security Analysis
- Avalanche Effect Testing
- Bit difference measurement
- Cipher quality evaluation

### File Encryption
- Encrypt text files
- Decrypt encrypted files
- Binary ciphertext output

### RSA Cryptography
- Public key generation
- Private key generation
- RSA encryption
- RSA decryption

### Hybrid Encryption
- Random session key generation
- Symmetric file encryption
- RSA session key protection
- Complete hybrid encryption workflow

---

## Project Structure

HybridCrypt/

├── main.py

├── cipher.py

├── key_schedule.py

├── utils.py

├── sbox.py

├── permutation.py

├── mix.py

├── avalanche.py

├── file_crypto.py

├── rsa.py

├── hybrid_crypto.py

├── README.md

└── .gitignore

---

## Encryption Pipeline

Plaintext

↓

XOR

↓

Bit Rotation

↓

S-Box Substitution

↓

Permutation

↓

Mix Layer

↓

Repeat Multiple Rounds

↓

Ciphertext

---

## Hybrid Encryption Workflow

File

↓

Generate Random Session Key

↓

Encrypt File Using Symmetric Cipher

↓

Encrypt Session Key Using RSA Public Key

↓

Store Encrypted Session Key + Ciphertext

↓

Hybrid Encrypted File

---

## Installation

Clone repository:

```bash
git clone https://github.com/vijaysimhareddy14/HybridCrypt.git
cd HybridCrypt