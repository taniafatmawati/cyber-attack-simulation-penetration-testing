#!/usr/bin/env python3
"""
Ping sweep (ICMP) - CLI-friendly, lab-only.
Requires --confirm to actually run (safety).
Uses utils.network_helpers.is_host_up() and logs to logs/ping_sweep.log.
"""
import argparse
from utils.network_helpers import is_host_up
from utils.logger import setup_logger
import ipaddress

def ping_sweep(subnet, timeout=1):
    logger = setup_logger("ping_sweep")
    logger.info(f"Starting ping sweep on {subnet}")

    try:
        net = ipaddress.ip_network(subnet, strict=False)
    except Exception as e:
        logger.error(f"Invalid subnet: {e}")
        return

    for ip in net.hosts():
        ip_str = str(ip)
        up = is_host_up(ip_str)
        if up:
            logger.info(f"[+] Host {ip_str} is UP")
        else:
            logger.debug(f"[-] Host {ip_str} is DOWN")

    logger.info("Ping sweep finished.")


def main():
    parser = argparse.ArgumentParser(description="Ping Sweep (ICMP) - lab-only")
    parser.add_argument("--subnet", required=True, help="Target subnet (e.g., 192.168.56.0/24)")
    parser.add_argument("--confirm", action="store_true", help="Confirm you will run this in a lab environment")
    parser.add_argument("--timeout", type=int, default=1, help="ICMP timeout in seconds (passed to helper)")
    args = parser.parse_args()

    if not args.confirm:
        print("[!] This script will send ICMP packets. Re-run with --confirm to proceed (lab-only).")
        print("Example: python attacks/ping_sweep.py --subnet 192.168.56.0/24 --confirm")
        return

    ping_sweep(args.subnet, timeout=args.timeout)

if __name__ == "__main__":
    main()
