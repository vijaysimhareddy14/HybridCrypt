# HybridCrypt 🔐

HybridCrypt is an educational cryptography project built entirely in Python. The project demonstrates how modern encryption systems work by combining a custom symmetric cipher with RSA public-key cryptography to create a hybrid encryption framework.

> ⚠️ Educational Project Only
> This project is designed for learning cryptography concepts and should not be used for protecting real-world sensitive information.

---

# Features

## Symmetric Encryption

* Multi-round encryption
* XOR-based key mixing
* Bit rotation operations
* S-Box substitution layer
* Permutation layer
* Diffusion mixing layer
* Key scheduling

## Security Analysis

* Avalanche effect testing
* Bit difference measurement
* Cipher quality evaluation

## File Encryption

* Encrypt text files
* Decrypt encrypted files
* Binary ciphertext output

## RSA Cryptography

* Public key generation
* Private key generation
* RSA encryption
* RSA decryption

## Hybrid Encryption

* Random session key generation
* Symmetric file encryption
* RSA session key protection
* Complete hybrid encryption workflow

---

# Project Architecture

```
                HYBRIDCRYPT

             ┌─────────────┐
             │ User File   │
             └──────┬──────┘
                    │
                    ▼
     Generate Random Session Key
                    │
     ┌──────────────┴──────────────┐
     │                             │
     ▼                             ▼
```

Custom Symmetric Cipher         RSA Encryption
(Fast Data Encryption)       (Protect Session Key)

```
     │                             │
     ▼                             ▼
```

Encrypted Data          Encrypted Session Key

```
     └──────────────┬──────────────┘
                    │
                    ▼

             Hybrid File (.hyb)

                    │
                    ▼

             Hybrid Decryption

     ┌──────────────┴──────────────┐
     │                             │
     ▼                             ▼
```

RSA Private Key              Session Key

```
     │                             │
     ▼                             ▼
```

Recover Session Key      Decrypt File Data

```
     └──────────────┬──────────────┘
                    │
                    ▼

              Original File
```

---

# Symmetric Cipher Architecture

Plaintext
│
▼
XOR Mixing
│
▼
Bit Rotation
│
▼
S-Box Substitution
│
▼
Permutation Layer
│
▼
Diffusion Mix Layer
│
▼
Repeat 12 Rounds
│
▼
Ciphertext

---

# Project Structure

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

# Encryption Workflow

1. User selects a file or enters text.
2. A random session key is generated.
3. The custom symmetric cipher encrypts the data.
4. RSA encrypts the session key using the public key.
5. The encrypted data and encrypted session key are stored together.
6. During decryption, RSA recovers the session key.
7. The recovered session key decrypts the original data.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/vijaysimhareddy14/HybridCrypt.git
cd HybridCrypt
```

Run the project:

```bash
python3 main.py
```

---

# Example

Encrypt Text

Input:

HELLO WORLD

Output:

8a91f3c2d7e4...

Decrypt Text

Output:

HELLO WORLD

---

# Avalanche Effect Testing

The project includes an avalanche testing module that measures how many output bits change when a single input bit is modified.

Example:

Changed Bits : 25

Total Bits   : 128

Avalanche %  : 19.53

This helps evaluate the diffusion properties of the cipher.

---

# Concepts Implemented

* Symmetric Encryption
* Asymmetric Encryption
* Hybrid Encryption
* RSA Cryptography
* Key Scheduling
* XOR Operations
* Bit Manipulation
* S-Box Substitution
* Permutation Networks
* Diffusion and Confusion
* Avalanche Effect Analysis
* File Encryption
* Multi-Round Cipher Design

---

# Learning Outcomes

This project helped in understanding:

* Internal structure of block ciphers
* Symmetric vs Asymmetric encryption
* RSA mathematics
* Hybrid encryption systems
* File encryption workflows
* Cryptographic design principles
* Software modularization in Python

---

# Future Improvements

* AES-style MixColumns implementation
* Larger block sizes
* CBC mode support
* CTR mode support
* SHA-256 integrity verification
* Digital signatures
* GUI application
* Secure randomized S-Boxes
* Performance optimization

---

# Author

**Koyyada Vijay Simha Reddy**
Bachelor of Engineering – Information Technology