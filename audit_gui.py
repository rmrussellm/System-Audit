import tkinter as tk
from tkinter import messagebox
import platform
import psutil
import socket
import os
import datetime
import threading  # <-- Add this

# --- System Info Functions ---

def get_os_info():
    return platform.platform()

def get_cpu_info():
    return platform.processor()

def get_ram_info():
    return f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"

def get_disk_info():
    disk = psutil.disk_usage('/')
    return f"Total: {round(disk.total / (1024 ** 3), 2)} GB, Free: {round(disk.free / (1024 ** 3), 2)} GB"

def get_ip_info():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unavailable"
    return f"{hostname} - {ip}"

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]

def list_installed_software():
    if os.name == 'nt':
        installed = os.popen('wmic product get name').read()
        return installed
    else:
        return "Installed software list only supported on Windows."

# --- Threaded Report Function ---
def run_audit():
    report = f"""
===============================
SYSTEM AUDIT REPORT
===============================

OS Info: {get_os_info()}
CPU: {get_cpu_info()}
RAM: {get_ram_info()}
Disk: {get_disk_info()}
Hostname/IP: {get_ip_info()}
Uptime: {get_uptime()}

Installed Software:
-------------------
{list_installed_software()}
"""
    with open("system_audit_report.txt", "w") as file:
        file.write(report)

    messagebox.showinfo("Success", "Report generated!\nSaved as system_audit_report.txt")

def generate_report_threaded():
    threading.Thread(target=run_audit).start()

# --- Tkinter GUI Setup ---
app = tk.Tk()
app.title("System Audit Report Tool")
app.geometry("400x200")

title_label = tk.Label(app, text="System Audit Report", font=("Arial", 14))
title_label.pack(pady=20)

generate_button = tk.Button(app, text="Generate Report", font=("Arial", 12), command=generate_report_threaded)
generate_button.pack(pady=10)

app.mainloop()