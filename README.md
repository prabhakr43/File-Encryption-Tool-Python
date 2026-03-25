File Encryption & Decryption Tool (AES-128)
Project Overview
This project is a professional-grade security utility developed as part of my Cybersecurity Internship at SkillFied Mentor. The tool is designed to ensure Data Confidentiality by implementing symmetric encryption, allowing users to protect sensitive files from unauthorized access.

Core Features
Secure Key Generation: Creates a unique 128-bit symmetric key using the Fernet (AES-128) specification.

File Lockdown: Transforms readable plaintext into unreadable ciphertext (binary format).

Data Integrity: Successfully restores encrypted data back to its original state using the authenticated secret key.

Menu-Driven Interface: User-friendly CLI for seamless operation.

Technical Stack
Language: Python 3.x

Library: cryptography (Fernet Implementation)

Algorithm: AES (Advanced Encryption Standard) in CBC mode with SHA256 HMAC for authentication.

How to Use
Installation: Install the required library using:

Bash
pip3 install cryptography
Setup: Run the script and select Option 1 to generate your secret.key.

Encrypt: Select Option 2 and enter the filename (e.g., test.txt) to secure your data.

Decrypt: Select Option 3 to revert the file to its original readable format.

Security Principle Applied
This tool demonstrates the practical application of Symmetric Cryptography. It highlights the importance of Key Management, as the security of the encrypted data relies entirely on the protection of the generated secret key.v
