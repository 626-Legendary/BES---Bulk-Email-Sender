# BES---Bulk-Email-Sender v1.0

This software allows you to send bulk emails using a specified list of recipients. It simulates the process of creating and sending emails through a desktop email client, leveraging Python's `pyautogui` library for automation of keyboard and mouse actions.

## Features
- Send bulk emails by reading recipient emails from a text area.
- Customizable send interval (in seconds) between each email.
- Logs all actions with timestamps.
- Option to save logs to a text file.
- User-friendly interface with `tkinter`.

## Installation

### Requirements
- Python 3.x
- Libraries:
  - `pyautogui`
  - `tkinter` (usually pre-installed with Python)
  - `threading`
  - `random`
  - `datetime`

You can install the required Python packages using `pip`:

```bash
pip install pyautogui

Usage
Recipients: Enter one recipient email per line in the "Recipients" text box.
Send Interval: Set the range (in seconds) for the time interval between sending emails.
Email Subject & Message Content: Fill in the subject and the message content.
Start Sending: Click the "Start Sending" button to begin sending emails.

Log: View logs of sent emails and any errors in the "Log" section.
Save Log: Click "Save Log" to save the log to a file.

Disclaimer
This software is for educational purposes only. The author is not responsible for any legal issues arising from the misuse of this software.

Version Information
Version: 1.0
Expiration Date: April 1, 2025
License
This project is open-source and provided "as is". Feel free to use and modify it as needed.

Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Issues and feature requests are also welcome.

Contact
If you have any questions, feel free to open an issue on this repository, or reach out via email.
