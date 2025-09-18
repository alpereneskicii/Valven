# Remote Command Execution over Socket (Python)

## 📌 About the Project

This project demonstrates a simple **client–server architecture** built with **Python sockets** that allows **remote command execution**.  
The server receives commands from connected clients, executes them, and returns the output.  
Each client runs in its own **session** with an isolated working directory.

---

## 📂 Project Structure
```bash

.
├── socket_client.py # Client code
├── socket_server.py # Server code
├── test_server.py # Unit tests for server commands
└── README.md # Project documentation
```

## 🚀 Setup & Run

### 1. Requirements

- Python 3.8+
- Works on Windows, Linux, and macOS

### 2. Start the Server

python socket_server.py

If successful, you will see:
```bash
[*] Server listening on <hostname>:5000
```


3. Start the Client

Open another terminal and run:
```bash
python socket_client.py
```
4. Usage

Enter a command in the client terminal → the server executes it and returns the output.

Quit with: q

🔑 Supported Commands

cd <directory> → Change working directory

cd → Print current directory

pwd → Show current directory

Other commands (ls, dir, echo, mkdir, etc.) are executed via subprocess.run


🧪 Testing

Tests are included in test_server.py.
Run them with:
```bash
python test_server.py
```

Tests cover:

pwd command

cd with valid/invalid directories

Empty command handling

Common commands like echo and dir

Session management

Sample output:
```bash
🔧 Starting Server Tests...
========================================
✅ PASS: pwd command works correctly
✅ PASS: CD command works
✅ PASS: Invalid directory error is shown
✅ PASS: Echo command works
✅ PASS: Session created successfully
...
🏁 All tests completed!
```
🧩 Architecture

Server

Handles multiple clients using threading

Keeps track of each client’s current_dir in a sessions dictionary

Client

Reads user input, sends it to the server, displays server output

Tests

Use tempfile for isolated test directories

⚠️ Security Notes

This project is for educational purposes only.
Running arbitrary remote commands is a serious security risk.
Do not use in production without:

Authentication

Encryption (TLS)

Proper access control & logging

