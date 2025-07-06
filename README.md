# System Audit Report Generator

A simple but powerful desktop app that gathers and exports key system information for help desk diagnostics, troubleshooting, and documentation.

---

## Features

- Collects system information:
  - Operating system version
  - CPU and RAM info
  - Disk usage (total & free)
  - Hostname and local IP address
  - System uptime
  - Installed applications (Windows)
- Clean, clickable GUI built with Tkinter
- Exports results to a readable `.txt` file
- Uses threading to keep the UI responsive

---

## Technologies Used

- **Python 3**
- **Tkinter** – GUI framework
- **psutil** – for RAM, disk, uptime
- **platform**, **socket**, **os**, **datetime** – built-in modules

---

##  Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/system-audit-tool.git
   cd system-audit-tool
