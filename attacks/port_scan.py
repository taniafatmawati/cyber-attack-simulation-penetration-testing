#!/usr/bin/env python3
"""
TCP Port Scanner - CLI-friendly, lab-only.
Requires --confirm. Uses utils.network_helpers.check_port() and logs to logs/port_scan.log.

Usage examples:
  python attacks/port_scan.py --target 192.168.56.101 --ports 22,80,443 --confirm
  python attacks/port_scan.py --target 127.0.0.1 --ports 1-1024 --confirm
"""
import argparse
from utils.network_helpers import check_port
from utils.logger import setup_logger
import re

def parse_ports(ports_str):
    """
    Parse ports argument.
    Accepts "22,80,443" or "1-1024" or combination "22,80,100-110".
    Returns sorted unique list of ints.
    """
    ports = set()
    parts = ports_str.split(",")
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.match(r"^(\d+)-(\d+)$", p)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            if start > end:
                start, end = end, start
            for port in range(start, end + 1):
                if 1 <= port <= 65535:
                    ports.add(port)
        else:
            try:
                port = int(p)
                if 1 <= port <= 65535:
                    ports.add(port)
            except ValueError:
                raise argparse.ArgumentTypeError(f"Invalid port token: {p}")
    return sorted(ports)

def port_scan(target, ports, timeout=0.5):
    logger = setup_logger("port_scan")
    logger.info(f"Starting port scan on {target} (ports: {len(ports)} entries)")

    open_ports = []
    for port in ports:
        try:
            is_open = check_port(target, port, timeout=timeout)
            if is_open:
                logger.info(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            else:
                logger.debug(f"[-] Port {port} closed")
        except Exception as e:
            logger.error(f"[!] Error scanning port {port}: {e}")

    logger.info(f"Port scan finished. Open ports: {open_ports}")

def main():
    parser = argparse.ArgumentParser(description="TCP Port Scan - lab-only")
    parser.add_argument("--target", required=True, help="Target host IP (e.g., 192.168.56.101)")
    parser.add_argument("--ports", default="1-1024", help="Ports to scan (e.g. '22,80,443' or '1-1024')")
    parser.add_argument("--timeout", type=float, default=0.5, help="TCP connect timeout in seconds (default 0.5)")
    parser.add_argument("--confirm", action="store_true", help="Confirm you will run this in a lab environment")
    args = parser.parse_args()

    if not args.confirm:
        print("[!] This script will attempt TCP connections. Re-run with --confirm to proceed (lab-only).")
        print("Example: python attacks/port_scan.py --target 127.0.0.1 --ports 1-1024 --confirm")
        return

    try:
        ports = parse_ports(args.ports)
    except Exception as e:
        print(f"[!] Invalid ports specification: {e}")
        return

    port_scan(args.target, ports, timeout=args.timeout)

if __name__ == "__main__":
    main()
