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
