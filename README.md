# Async HTTP Load Testing Tool (Educational Use Only)

An asynchronous Python-based CLI tool built with `asyncio` and `aiohttp`, designed for **HTTP load testing and concurrency experiments**.

This project focuses on learning and demonstrating **asynchronous programming**, **request concurrency**, and **network behavior under load**.

---

## Features

- Asynchronous HTTP requests using `aiohttp`
- Configurable total requests and concurrent connections
- Randomized User-Agent per request to simulate real traffic
- Continuous request loop for sustained load testing
- Lightweight and easy-to-run CLI interface

---

## Example

```text
.__            __    __                 __    
|  |__ _____ _/  |__/  |______    ____ |  | __
|  |  \\__  \\   __\   __\__  \ _/ ___\|  |/ /
|   Y  \/ __ \|  |  |  |  / __ \\  \___|    < 
|___|  (____  /__|  |__| (____  /\___  >__|_ \
     \/     \/                \/     \/     \/



[Configuration]
Examples: requests=1000 | concurrency=100

[13:35:08] Starting configuration...

› Target URL            (e.g. https://example.com) : https://example.com
› Total requests        (e.g. 1000) : 1000
› Concurrent connections(e.g. 100) : 100

────────────────────────────────────────────────────
 Target URL   : https://example.com
 Requests     : 1000
 Concurrency  : 100
────────────────────────────────────────────────────


[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
[OK] [13:35:24] Status: 200
```

---

## Installation & Usage

### Requirements
- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/pangeran-droid/HTTP-Flood-Attack.git
cd HTTP-Flood-Attack
pip install aiohttp
chmod +x tester.py
./tester.py
```

> **Windows users:**  
> If `python3` is not available, run the script using:
> ```bash
> python tester.py
> ```

---

## ⚠️ Disclaimer & Legal Notice

**This tool is created strictly for educational and research purposes.**

### ✅ Allowed Use

- Load testing servers you own or have permission to test
- Simulating traffic for development and performance evaluation
- Learning asynchronous programming and networking concepts in Python

### ❌ Prohibited Use

- Attacking, disrupting, or degrading third-party systems
- Any activity that violates laws, regulations, or terms of service

> **Any misuse of this tool is solely the responsibility of the user.**
The developer assumes no liability for illegal or unethical use.



