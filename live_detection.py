from scapy.all import sniff
import joblib
import numpy as np

# Load pre-trained model and scaler
model = joblib.load('anomaly_detection_model.pkl')
scaler = joblib.load('scaler.pkl')

def detect_anomaly(packet):
    if packet.haslayer(IP):
        src_port = packet.sport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
        dst_port = packet.dport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
        protocol = packet[IP].proto
        length = len(packet)

        # Scale features
        features = np.array([[src_port, dst_port, protocol, length]])
        scaled_features = scaler.transform(features)

        # Predict anomaly
        prediction = model.predict(scaled_features)
        if prediction == -1:
            print(f"🚨 ANOMALY DETECTED: {packet.summary()}")

# Start live detection
sniff(iface="eth0", prn=detect_anomaly, store=0)
