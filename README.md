# File Integrity Checker

## Description
File Integrity Checker is a tool designed to monitor and verify the integrity of files in your system. It helps in identifying unauthorized changes, ensuring that your files remain unchanged over time. This project aims to provide users with a reliable way to maintain file integrity, which is crucial for data security and compliance.

## Features
- **Real-time Monitoring:** Continuously checks file integrity and notifies about unauthorized changes.
- **Detailed Reporting:** Provides logs and detailed reports of any changes detected.
- **Customizable Settings:** Users can configure which files or directories to monitor.
- **Cross-Platform Compatibility:** Works on various operating systems including Windows, Linux, and macOS.

## Project Structure
```
File-Integrity-Checker/
├── src/                  # Source code
├── tests/                # Unit tests
├── docs/                 # Documentation
├── README.md             # Project documentation
└── LICENSE               # License information
```

## Installation
To install the File Integrity Checker, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Muthu-Khader/File-Integrity-Checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd File-Integrity-Checker
   ```
3. Install required dependencies:
   ```bash
   npm install
   ```

## Usage
To start monitoring files, run:
```bash
node src/monitor.js
```
You can specify the files or directories to monitor in the configuration file located at `config.json`.

## How It Works
File Integrity Checker uses hashing algorithms to create a snapshot of files when they are first monitored. On subsequent scans, it compares the current file hashes with the original to detect any changes.

## Security Features
- **Encryption:** Sensitive information is encrypted to protect against unauthorized access.
- **Access Control:** Only authorized users can configure and access the monitoring settings.
- **Log Management:** All integrity checks are logged securely for audit purposes.

## Contributing Guidelines
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Add your changes and commit:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.