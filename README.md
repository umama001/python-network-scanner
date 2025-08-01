# 🌐 Simple Python Network Scanner (Ping Scan)

This Python script is a basic network scanner that helps you discover active hosts (devices) within a specified IP address range using `ping` commands. It's a fundamental tool for understanding network basics and Python's interaction with the operating system.

### 🚀 Features

* ✅ **IP Range Scanning:** Scans a user-defined range of IP addresses (e.g., 192.168.1.1 to 192.168.1.254).
* ✅ **Active Host Detection:** Identifies which hosts within the range are "UP" (responding to ping requests) or "DOWN".
* ✅ **Cross-Platform Compatibility:** Automatically adjusts `ping` command parameters (`-n` for Windows, `-c` for Linux/macOS).
* ✅ **Command-Line Arguments:** Takes network prefix and IP range as arguments for easy execution.
* ✅ **Error Handling:** Basic validation for IP format and range.
* ✅ **Scan Summary:** Provides a clear list of all active hosts found after the scan.

---

### 💻 How to Use

This script is run from the command line (terminal) and requires you to provide the network prefix and the starting/ending IP octets.

🔧 **Command-Line Usage:**

```bash
python3 network_scanner.py <network_prefix> <start_last_octet> <end_last_octet>

<network_prefix>: The common part of the IP address (e.g., "192.168.1."). Remember to include the final dot.

<start_last_octet>: The starting number for the last part of the IP address (e.g., 1).

<end_last_octet>: The ending number for the last part of the IP address (e.g., 254).

Example Execution:

To scan IPs from 192.168.1.1 to 192.168.1.254:
    python3 network_scanner.py 192.168.1. 1 254
Expected Output (Example):

Scanning network: 192.168.1.1-254
Host 192.168.1.1: UP
Host 192.168.1.2: DOWN
Host 192.168.1.3: UP
...
Host 192.168.1.254: DOWN

--- Scan Summary ---
Active hosts found:
- 192.168.1.1
- 192.168.1.3
Requirements:

🐍 Python 3.x installed on your system.

🖥️ A command-line interface (Terminal on Linux/macOS, Command Prompt/PowerShell on Windows).

📚 What You'll Learn
Working with this project is an excellent way to understand fundamental programming and networking concepts:

🐍 Python subprocess Module: Learn how to run external system commands (like ping) from your Python script and capture their output.

💻 Platform Detection (platform module): Understand how to write cross-platform code by detecting the operating system.

🧩 Regular Expressions (re module): Practice using regex for basic input validation (e.g., checking IP address format).

⚙️ Command-Line Arguments (sys module): Learn to pass arguments to your Python script directly from the terminal.

🌐 Basic Networking Concepts: Get a hands-on understanding of how ping works to identify active devices on a network.

🐛 Error Handling: Implement try-except blocks to manage potential issues like network timeouts or invalid input.

🚀 Future Enhancements (Ideas)
Consider these ideas to expand the functionality and complexity of this project:

📈 Multi-threading/Asynchronous Scanning: Implement concurrent pinging to speed up the scan process significantly.

🔍 Port Scanning: Add functionality to scan open ports on active hosts (e.g., using socket module).

📊 Output to File: Allow users to save the scan results to a text file or a more structured format (CSV, JSON).

🖥️ GUI Interface: Develop a graphical user interface using libraries like tkinter or PyQt for a more user-friendly experience.

🗺️ Network Discovery: Integrate more advanced network protocols (like ARP for local network discovery).

📡 Hostname Resolution: Resolve IP addresses to hostnames (if available on the network).

🛠️👣 How to Try This Project (Step-by-Step)
If you'd like to run and experiment with this project on your own system, here's a simple guide:

Go to this project’s GitHub page.

Click the green “Code” button and then choose “Download ZIP”.

Extract the downloaded ZIP file to a folder on your computer.

Open your terminal (Command Prompt, PowerShell on Windows, or Terminal on Linux/macOS).

Navigate into the project folder using the cd command. For example:
    cd path/to/your/network_scanner_project
(Remember to replace path/to/your/network_scanner_project with the actual path to the folder where you extracted the project.)

Verify Python installation by typing:
    python3 --version

Run the script with the appropriate arguments. For example, to scan your local network from 192.168.1.1 to 192.168.1.254:
    python3 network_scanner.py 192.168.1. 1 254
Note for Windows users: If python3 doesn't work, try running the script with just python: python network_scanner.py 192.168.1. 1 254.

⚠️ Disclaimer
This tool is created for educational and learning purposes only.

It performs basic network scanning (ping). Always ensure you have permission before scanning any network, especially one you do not own or manage. Unauthorized network scanning may be considered illegal or unethical.

The script provides simple 'UP' or 'DOWN' status based on ping responses and should not be used for critical security assessments.
