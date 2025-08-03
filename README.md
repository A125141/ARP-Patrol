# 🛡️ ARP Detector - GUI Based

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

---

## 📁 Project Structure

arp-detector/
├── main.py # Core logic & sniffer
├── gui.py # GUI code (CustomTkinter)
├── images/
│ └── Icon.ico # App icon
├── README.md

yaml
Copy code

---

## 💻 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
Or manually install:

bash
Copy code
pip install scapy customtkinter dark-title-bar pillow win10toast
Note: win10toast only works on Windows

▶️ Run the App
Run the app using Python:

bash
Copy code
python main.py
🛠️ Convert to EXE (Optional)
You can bundle the project into a single .exe file with no external dependencies using PyInstaller:

bash
Copy code
pyinstaller --onefile --windowed --add-data "images/Icon.ico;images" main.py
Make sure --add-data path is correct depending on your OS.
For Windows: use semicolon ;
For macOS/Linux: use colon :

If you want to avoid using external folders for images, you can:

Convert the image (e.g., Icon.ico) to base64

Load it directly in code using BytesIO

🧠 Tips to Prevent ARP Spoofing
Displayed inside the app GUI:

vbnet
Copy code
🔵 Try to disconnect the network cable from the router  
🔵 Turn on Airplane Mode in your device  
🔵 Change your device's IP address  
🔵 Monitor packets with Wireshark  
🔵 Use static ARP entries (advanced)



👨‍💻 Author
Developed by A125141
GitHub: github.com/A125141

Feel free to fork or contribute.
Pull requests are welcome!
