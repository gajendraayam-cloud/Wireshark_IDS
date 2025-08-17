# wireshark_ids.py
import subprocess
import re

def capture_packets(interface="eth0", count=50):
    cmd = ["tshark", "-i", interface, "-c", str(count)]
    output = subprocess.check_output(cmd, text=True)
    return output.splitlines()

def detect_syn_flood(packets):
    syn_count = sum(1 for pkt in packets if "SYN" in pkt and "ACK" not in pkt)
    if syn_count > 20:
        print("[ALERT] Possible SYN flood detected!")
    else:
        print("Traffic normal.")

if __name__ == "__main__":
    print("Capturing packets... (requires sudo)")
    packets = capture_packets("wlan0", count=100)
    detect_syn_flood(packets)
