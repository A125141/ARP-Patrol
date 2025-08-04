# 🛡️ ARP Detector

A simple Python tool to detect ARP spoofing/poisoning attacks in real time using a graphical user interface.

---

## ⚙️ Features

- ✅ Live ARP packet sniffing using **Scapy**
- ✅ Detects ARP spoofing by comparing real MACs with spoofed packets
- ✅ Toast notifications for attacks (Windows only)
- ✅ Clean GUI using **customtkinter**
- ✅ Security tips to mitigate ARP attacks
- ✅ Lightweight, runs in the background

---

## 🖼️ User Interface

> The interface displays the current ARP table and helpful instructions to defend against ARP poisoning. It also includes buttons to start and stop monitoring.

Example layout:
IP Address MAC Address
192.168.1.1 AA:BB:CC:DD:EE:FF
192.168.1.2 11:22:33:44:55:66
...

yaml
Copy code

GUI also includes:
- Start Monitoring / Stop Monitoring buttons  
- ARP protection tips section  
- Developer signature

---

## 🧠 How It Works

1. Reads the local ARP table using `arp -a`
2. Continuously sniffs ARP packets using `scapy`
3. Compares each ARP reply's MAC with known MACs
4. If a mismatch is found:
   - Logs details of the suspicious packet
   - Sends a toast notification (if enabled)
5. Displays the real-time ARP table in the GUI

6. 


👨‍💻 Author
Developed by A125141
GitHub: github.com/A125141

Feel free to fork or contribute.
Pull requests are welcome!
