# Brute-Force Log Detector
Python tool that analyzes server logs to detect brute-force login attacks.

## How it works
- pip install rich
- python detectory.py
- Reads logs.txt
- Extracts failed logins with regex
- Counts failures per IP using Counter
- Alerts if IP fails >= 3 times

## Screenshot
![scan] (screenshot.jpg)

## Skills demonstrated
Python, Regex, Log Analysis, Incident Detection
