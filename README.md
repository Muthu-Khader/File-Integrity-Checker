# 🔐File Integrity Checker

## 📌Description
A CLI-based File Integrity Monitoring tool built using Python that detects file modifications, additions, and deletions using SHA-256 hashing.

This tool creates a baseline snapshot of file hashes and compares future scans to identify any unauthorized or unexpected changes.

## 🚀 Features
*🔍 Scan files and folders*🧠 Baseline creation for integrity tracking
*⚠️ Detect:
    *Modified files
    *New files
    *Deleted files
*👤 User-controlled updates for security
*🧱 Modular architecture (clean code design)
*💻 Command Line Interface (CLI)

## 🛠️ Tech Stack
*Python
*hashlib (SHA-256)
*os, sys (file system + CLI)
*JSON (data storage)

## 📂Project Structure
```
File-Integrity-Checker/
├── main.py/                  # CLI Entry point
├── core.py/                  # Logic (compare, load, save) 
├── scanner.py/               # File Scanning
├── hash_utils.py/            # Hash generation
├── utils.py/                 # Helper functions
└── database.json             # Stores file hashes (ignored in git)
```

## ⚙️Installation
To install the File Integrity Checker, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Muthu-Khader/File-Integrity-Checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd File-Integrity-Checker
   ```
3. Run the Tool:
   ```bash
   python main.py scan <path>
   ```

## 🧪Usage
Scan a folder:
```bash
python main.py scan "test folder"
```
Scan a single file:
```bash
python main.py scan test.txt
```

## 🧠How It Works
1. The tool scans files and generates SHA-256 hashes
2. Stores hashes as a baseline in database.json
3. On next scan:
     *Compares current hashes with stored hashes
     *Detects changes (modified, new, deleted)
4.Prompts user before updating baseline (for security)

## 🔐Security Features
This tool follows a baseline integrity model, where:
*Initial scan = trusted state
*Future scans = verification against baseline

## 💼 Use Case
*Detect unauthorized file changes
*Monitor important system/project files
*Learn file integrity concepts in cybersecurity

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
