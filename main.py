from gui import ArpDetectorGUI, get_arp_dict
from scapy.all import sniff, ARP
from time import gmtime, strftime
import threading
from win10toast import ToastNotifier

# Initialize ARP dictionary
arp = {}
# Variable to track monitoring state
monitoring = False

def check_attack(x):
    if ARP in x and x[ARP].op == 2:
        hwsrc = x.sprintf("%ARP.hwsrc%")
        psrc = x.sprintf("%ARP.psrc%")
        hwdst = x.sprintf("%ARP.hwdst%")
        pdst = x.sprintf("%ARP.pdst%")
        if psrc in arp:
            if arp[psrc] != hwsrc:
                message = "{} want {}\nBut {} is {}\n\nTarget {} ({})".format(hwsrc, psrc, psrc, arp[psrc], hwdst, pdst)
                print("{} ; {} want {} ; But {} is {} ; Target {} ({})".format(strftime("%Y/%m/%d %H:%M:%S", gmtime()), hwsrc, psrc, psrc, arp[psrc], hwdst, pdst))
                # Show Windows notification if monitoring is enabled
                if monitoring:
                    toaster = ToastNotifier()
                    toaster.show_toast("ARP Poisoning Attack Detected",
                                       "{} wants to impersonate as {}\n\nTarget: {} ({})".format(hwsrc, psrc, pdst, hwdst),
                                       duration=10)
        else:
            arp[psrc] = hwsrc

def run_sniffer():
    global monitoring
    # Sniffing ARP packets
    sniff(prn=check_attack, filter="arp", store=0)
    monitoring = False

def on_start_clicked():
    global monitoring
    if not monitoring:
        # Start ARP monitoring in a separate thread
        monitoring = True
        threading.Thread(target=run_sniffer, daemon=True).start()

def on_stop_clicked():
    global monitoring
    # Stop ARP monitoring
    monitoring = False

def main():
    global arp
    # Get ARP dictionary
    arp = get_arp_dict()

    # Create GUI instance
    gui = ArpDetectorGUI(arp, on_start_clicked, on_stop_clicked)
    gui.display_arp_table()

if __name__ == "__main__":
    main()
