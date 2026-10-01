from rich import print
from rich.panel import Panel
from collections import Counter
import re

"""
Brute-Force Attack Detector
Author: Zacarias Eduardo Joao
Description: Analyzes auth logs and detects IPs with multiple failed login attempts.
Usage: python brute_force_detector.py
Log format expected: "Login failed - IP: 192.168.1.10"
"""

print("=== BRUTE-FORCE DETECTOR ===\n")

# Load log file
try:
    with open("logs.txt", "r") as f:
        logs = f.readlines()
except FileNotFoundError:
    print("[red]Error: logs.txt file not found. Please create the log file first![/]")
    exit()

# Filter failed login attempts
failed_attempts = []
failed_ips = []

for line in logs:
    if "Login failed" in line:
        failed_attempts.append(line)
        ip_match = re.search(r'IP:\s*(\d+\.\d+\.\d+\.\d+)', line)
        if ip_match:
            failed_ips.append(ip_match.group(1))

print(f"Total failed attempts found: {len(failed_attempts)}")

# Count failures per IP
ip_counter = Counter(failed_ips)

report_content = ""
attack_detected = False

for ip, count in ip_counter.items():
    if count >= 3: # Threshold for brute-force
        report_content += f"[!] ALERT: IP [red]{ip}[/] attempted {count} times - POSSIBLE BRUTE-FORCE\n"
        attack_detected = True
    else:
        print(f"[OK] IP {ip} - {count} attempt(s)")

print()
print(Panel(report_content if report_content else "No suspicious activity.", title="--- SUSPICIOUS IP REPORT ---", width=80, padding=1))

if attack_detected:
    print("\n[yellow]>>> RECOMMENDED ACTION: Block listed IPs on firewall <<< [/]")
else:
    print("\nNo attack detected.")

# Save report
with open("security_report.txt", "w") as out:
    out.write("SECURITY REPORT - BRUTE-FORCE ANALYSIS\n")
    for ip, count in ip_counter.items():
        out.write(f"{ip} - {count} failed attempts\n")

print("\n[green]Report saved to security_report.txt[/]")
