from customtkinter import CTk, CTkButton
import subprocess
import re
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from customtkinter import *
from dark_title_bar import *

class ArpDetectorGUI:
    def __init__(self, arp_dict, start_callback, stop_callback):
        self.arp = arp_dict
        self.start_callback = start_callback
        self.stop_callback = stop_callback

    def display_arp_table(self):
        root = CTk()
        root.title("ARP Detector")
        root.geometry("470x580")

        # Create ARP table display
        arp_table_label = Label(root, text="ARP Table:", font=("Arial", 14, "bold"))
        arp_table_label.configure(bg="#3A6BFF", fg="#3A6BFF")
        arp_table_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        arp_label = Label(root, text="Tips to prevent ARP Attack:", font=("Arial", 14, "bold"))
        arp_label.configure(bg="#242424", fg="#ffffff")
        arp_label.place(x=12 , y=310)

        arp_label = Label(root, text='''🔵 Try to Disconect the network cable from the router.
🔵 Turn on the Airplane Mode in your Device.
🔵 Try to change the IP address of your Device.
🔵 Check More info about the attack using wireshark. 
🔵 Change your IP Address                 


''', font=("Arial", 12) , justify="left")
        arp_label.configure(bg="#242424", fg="#ffffff")
        arp_label.place(x=12 , y=350)
        
        arp_label = Label(root, text='''By A125141''', font=("Arial", 9) , justify="left")
        arp_label.configure(bg="#242424", fg="#ffffff")
        arp_label.place(x=12 , y=560)        

        arp_table_text = Text(root, height=10, width=50, font=("Arial", 12))
        arp_table_label.configure(bg="#242424", fg="#ffffff")
        arp_table_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Populate ARP table
        arp_table_text.insert(END, "IP Address\t\tMAC Address\n")
        arp_table_text.insert(END, "-" * 40 + "\n")
        for ip, mac in self.arp.items():
            arp_table_text.insert(END, f"{ip.ljust(15)}\t{mac}\n")

        # Create Start and Stop buttons
        start_button = CTkButton(root, text="Start Monitoring", font=("Arial", 12, "bold"))
        start_button.grid(row=2, column=0, padx=10, pady=10)
        start_button.configure(bg_color="#000000", fg_color="#3A6BFF")
        start_button.configure(command=self.start_callback)

        stop_button = CTkButton(root, text="Stop Monitoring", font=("Arial", 12, "bold"))
        stop_button.grid(row=2, column=1, padx=10, pady=10)
        stop_button.configure(bg_color="#000000", fg_color="#3A6BFF")
        stop_button.configure(command=self.stop_callback)

        root.mainloop()

def get_arp_dict():
    arp_dict = {}
    arp_output = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    for line in arp_output.stdout.split("\n"):
        match = re.match(r'^\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s+([0-9A-Fa-f:-]+)\s+.*$', line)
        if match:
            ip, mac = match.groups()
            arp_dict[ip] = mac
    return arp_dict
