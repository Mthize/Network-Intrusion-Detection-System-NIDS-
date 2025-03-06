# Network Anomaly Detection System

## Description
This project implements a Network Anomaly Detection System using Suricata for signature-based threat detection and Machine Learning for anomaly detection.

## Features
- Network packet capture using Scapy
- Signature-based threat detection with Suricata
- Anomaly detection using Isolation Forest
- Real-time detection pipeline
- Traffic visualization with Matplotlib
- Optional integration with Kibana

## Technologies Used
- Python
- Scapy
- Suricata
- Pandas
- Scikit-learn
- TensorFlow
- Matplotlib
- Jupyter

## Installation
### Set Up the Environment
1. Install Dependencies:
   ```bash
   # Install Suricata (Ubuntu/Debian)
   sudo apt-get update
   sudo apt-get install suricata -y

   # Install Python libraries
   pip install scapy pandas scikit-learn tensorflow matplotlib jupyter
   ```


### Visualize Results (Optional)
```python
import matplotlib.pyplot as plt

data = pd.read_csv('network_traffic.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)
data['length'].resample('1T').sum().plot()
plt.title('Network Traffic Over Time')
plt.show()
```

### Simulate Attacks for Testing
Port Scan (using hping3):
```bash
sudo hping3 -S -p 80 --flood 192.168.1.1
```

Check Alerts:
- Suricata logs: `/var/log/suricata/fast.log`
- ML anomalies: Output from `live_detection.py`

## Contact
- Name: Thapelo Mthize
- Email: cyber_shield@icloud.com
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/thapelomthize)

