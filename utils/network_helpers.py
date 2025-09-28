#!/usr/bin/env python3
import socket
import subprocess

def is_host_up(ip):
    """
    Simple ICMP ping check using system ping command.
    Returns True if host responds, False otherwise.
    """
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", ip],
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

def check_port(ip, port, timeout=0.5):
    """
    Check if a TCP port is open.
    Returns True if open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

