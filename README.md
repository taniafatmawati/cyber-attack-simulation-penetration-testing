# 🚀 Cyber Attack Simulation for Penetration Testing on Kali Linux

## Overview

This project is an educational simulation of common cyberattacks, implemented for learning purposes and to understand penetration testing techniques. The goal is to:

- Understand vulnerabilities in servers and networks.
- Learn how common attacks work in controlled environments.
- Analyze defensive measures and security hardening effectiveness.

**⚠️ Disclaimer:**  
This project is strictly for educational purposes. Do not use these scripts on unauthorized systems. Misuse can be illegal and unethical.

---

## Features / Simulated Attacks

1. **Ping Sweep (ICMP)**
   - Simulates network reconnaissance using ICMP echo requests.
   - Detects active hosts in a subnet.

2. **TCP Port Scan**
   - Simulates a basic TCP port scan to identify open ports on a target host.
   - Helps understand attack surface enumeration.

3. **SSH Brute Force (Simulation)**
   - Attempts password login with a small list of sample passwords on a local test server.
   - Shows how brute force works and the importance of strong credentials.

4. **Safe DoS Simulation**
   - Demonstrates a Denial of Service attack in a controlled local test environment.
   - Monitors system behavior without harming production services.

---

## Requirements

- **Kali Linux** (tested on 2023.3+)
- Python 3.10+
- `scapy` for packet crafting and analysis
- `paramiko` for SSH simulation
- `socket` and `subprocess` modules for network tasks

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/taniafatmawati/cyber-attack-simulation-kali.git
cd cyber-attack-simulation-kali
````

2. Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage Examples

**Ping Sweep Example:**

```bash
python attacks/ping_sweep.py --subnet 192.168.56.0/24
```

**Port Scan Example:**

```bash
python attacks/port_scan.py --target 192.168.56.101 --ports 20-1024
```

**SSH Brute Force Simulation Example:**

```bash
python attacks/brute_force_ssh.py --host 127.0.0.1 --user testuser --passwords passwords.txt
```

**Safe DoS Simulation Example:**

```bash
python attacks/dos_simulation.py --target 127.0.0.1 --count 50
```

---

## Learning Outcomes

* Understand network reconnaissance and enumeration.
* Learn the mechanics behind brute force and DoS attacks.
* Explore how defensive measures can mitigate common attacks.
* Enhance Python scripting skills for cybersecurity applications.

---




## 🛠️ Steps to Implement

### Environment Setup

Install Kali Linux:
1. Download from the official website.
2. Follow the installation instructions.

Update System:
```bash
sudo apt update && sudo apt upgrade -y
```

Install Penetration Testing Tools:
```bash
sudo apt install nmap ncat hping3 ettercap-common ettercap-graphical bettercap wireshark
sudo apt install hydra
sudo apt install git
sudo apt install sqlmap
sudo apt install gobuster
```

### Execute Attack Simulations

1. **Brute-Force Attack:**
   - Description: Attempts to gain unauthorized access by trying numerous password combinations.
   - Impact: Can compromise user accounts if weak passwords are used.
   - Target: SSH service.
   - Command:
     ```bash
     hydra -l <username> -P <password_list> ssh://<TARGET_IP>
     ```
     
2. **Firewall Bypass Attempt:**
   - Description: Tests if firewall rules can be evaded.
   - Impact: Potentially exposes services that should be protected by the firewall.
   - Target: Open ports through firewall.
   - Commands:

     Identify firewall rules:
     ```bash
     nmap -p- <TARGET_IP>
     ```

     Attempt bypass:
     ```bash
     nmap -f -p <TARGET_PORT> <TARGET_IP>
     ```
     
3. **Denial of Service (DoS) Attack:**
   - Description: Overwhelms a service to make it unavailable.
   - Impact: Service disruption or downtime.
   - Target: Web server or application.
   - Commands:

     Using hping3:
     ```bash
     sudo hping3 --flood -p 80 <TARGET_IP>
     ```
   
4. **Man-in-the-Middle (MitM) Attack:**
   - Description: Intercepts and manipulates communication between two parties.
   - Impact: Data leakage or alteration.
   - Target: Network traffic between clients and servers.
   - Commands:

     Use Ettercap:
     ```bash
     sudo ettercap -T -M arp:remote /<TARGET_IP>/ /<GATEWAY_IP>/
     ```

     Capture traffic:
     ```bash
     sudo tcpdump -i eth0 -w /root/mitm_data.pcap
     ```

     Analyze with Wireshark:
     ```bash
     sudo wireshark /root/mitm_data.pcap
     ```
     
5. **SQL Injection:**
   - Description: Injects malicious SQL queries to manipulate a database.
   - Impact: Unauthorized access to database or data corruption.
   - Target: Web applications with SQL databases.
   - Command:
     ```bash
     sqlmap -u "<TARGET_URL>" --dbs
     ```

6. **Network Sniffing:**
   - Description: Captures and analyzes network traffic to extract sensitive information.
   - Impact: Exposure of unencrypted data.
   - Target: Network traffic.
   - Command:
     ```bash
     sudo tcpdump -i eth0 -w /root/network_traffic.pcap
     ```

7. **Session Hijacking:**
    - Description: Takes over an active user session.
    - Impact: Unauthorized access to user accounts and data.
    - Target: Web sessions.
    - Command:
      ```bash
      sudo ettercap -T -M arp:remote /<TARGET_IP>/ /<GATEWAY_IP>/
      ```

8. **Exploit Remote Code Execution (RCE):**
    - Description: Exploits a vulnerability to execute arbitrary commands on a remote system.
    - Impact: Full control over the remote system.
    - Target: Remote servers with RCE vulnerabilities.
    - Command:
      ```bash
      msfconsole
      use exploit/linux/http/<exploit_module>
      set RHOSTS <TARGET_IP>
      exploit
      ```
      
9. **Password Cracking:**
    - Description: Uses various techniques to recover passwords from hashes.
    - Impact: Compromise of user accounts.
    - Target: Password hashes.
    - Command:
      ```bash
      john --wordlist=<wordlist> <hash_file>
      ```

10. **Wi-Fi Network Attack:**
    - Description: Attacks Wi-Fi networks to crack passwords or intercept traffic.
    - Impact: Unauthorized access to network and data.
    - Target: Wi-Fi networks.
    - Command:
      ```bash
      aircrack-ng -w <wordlist> -b <BSSID> <capture_file>
      ```

11. **DNS Spoofing:**
    - Description: Redirects DNS requests to malicious servers.
    - Impact: Phishing or data interception.
    - Target: DNS traffic.
    - Command:
      ```bash
      sudo ettercap -T -M arp:remote /<TARGET_IP>/ /<DNS_SERVER_IP>/
      ```

12. **Web Application Scanning:**
    - Description: Scans web applications for vulnerabilities.
    - Impact: Identifies weaknesses for further exploitation.
    - Target: Web applications.
    - Command:
      ```bash
      nikto -h <TARGET_URL>
      ```

## 📬 Contact 

If you have any questions or suggestions, feel free to reach out:

- ✉️ Email: tania.fatmawati20@gmail.com
- 🔗 LinkedIn: linkedin.com/in/tania-fatma-wati/
- 💻 GitHub: github.com/taniafatmawati

Thank you for exploring my Cyber Attack Simulation documentation!
