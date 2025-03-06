from scapy.all import sniff, IP, TCP, UDP
import pandas as pd

# Initialize DataFrame to store packet data
columns = ['timestamp', 'src_ip', 'dst_ip', 'src_port', 'dst_port', 'protocol', 'length']
packet_df = pd.DataFrame(columns=columns)

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)

        src_port = None
        dst_port = None
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        # Append packet data to DataFrame
        global packet_df
        packet_df = pd.concat([packet_df, pd.DataFrame([{
            'timestamp': pd.Timestamp.now(),
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'src_port': src_port,
            'dst_port': dst_port,
            'protocol': protocol,
            'length': length
        }])], ignore_index=True)

# Start capturing (adjust interface and filter)
sniff(iface="eth0", prn=packet_handler, store=0, count=1000)  # Capture 1000 packets

# Save to CSV for ML training
packet_df.to_csv('network_traffic.csv', index=False)
