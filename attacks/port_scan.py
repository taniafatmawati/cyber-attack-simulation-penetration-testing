#!/usr/bin/env python3
import scapy.all as scapy
import argparse

def ping_sweep(subnet):
    print(f"Starting ping sweep on {subnet}...")
    for ip in scapy.IPNetwork(subnet):
        packet = scapy.IP(dst=str(ip))/scapy.ICMP()
        response = scapy.sr1(packet, timeout=1, verbose=0)
        if response:
            print(f"[+] Host {ip} is up.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ping Sweep Simulation")
    parser.add_argument("--subnet", required=True, help="Target subnet (e.g., 192.168.56.0/24)")
    args = parser.parse_args()
    ping_sweep(args.subnet)
