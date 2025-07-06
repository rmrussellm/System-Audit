import platform
import psutil
import socket
import os
import datetime

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
    return str(uptime).split('.')[0]  # Remove microseconds

def list_installed_software():
    if os.name == 'nt':  # Windows only
        installed = os.popen('wmic product get name').read()
        return installed
    else:
        return "Installed software list only supported on Windows."

def generate_report():
    print("Generating System Audit Report...\n")
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

    print("✅ Report saved as system_audit_report.txt")

generate_report()