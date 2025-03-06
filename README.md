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


Here's a detailed text-based mock-up of both dashboards for you to visualize or use as inspiration to structure your own. I've included key sections and design tips for an appealing layout.

---

### **Suricata Alerts Dashboard Mock-Up**  
+================================================================================================+  
| **SURICATA ALERTS DASHBOARD**                                                                 |  
+=======================+=============================+=======================+=================+  
| **[Real-Time Alerts]**    | **[Geo Threat Map]**        | **[Top Alert Types]**   | **[Severity Distribution]** |  
|---------------------------|----------------------------|-------------------------|----------------------------|  
| Timestamp: 12:05:03       | (World Map with glowing    | 1. **ET Malware** ────▓ | **High** ▓▓▓▓▓▓▓           |  
| Source: 192.168.1.5       | red dots over US, RU, CN)  | 2. **SQL Injection** ───▓ | **Critical** ▓▓▓▓▓▓▓▓▓     |  
| Dest: 10.0.0.12           |                            | 3. **Port Scan** ───────▓ | **Medium** ▓▓▓▓            |  
| Alert: SQL Injection      |                            |                         | **Low** ▓                   |  
|---------------------------|----------------------------|-------------------------|----------------------------|  
| Timestamp: 12:05:10       | **[Traffic Flow]**         | **[Packet Stats]**      | **[Action Log]**           |  
| Source: 10.0.0.42         | (Line chart: spikes at     | Total: 12K pkts         | Blocked: 15 IPs            |  
| Dest: 192.168.1.100       | 12:05)                     | Alerts: 45              | Allowed: 2                 |  
| Alert: ET Exploit         |                            |                         |                            |  
+===========================+============================+=========================+============================+  

---

### **ML Monitoring Dashboard Mock-Up**  
+================================================================================================+  
| **MACHINE LEARNING MONITORING DASHBOARD**                                                        |  
+=======================+=============================+=======================+=================+  
| **[Model Performance]**   | **[Feature Importance]**     | **[Data Drift]**       | **[Confusion Matrix]**     |  
|---------------------------|-----------------------------|------------------------|---------------------------|  
| Accuracy: 94.5% ▲         | 1. **User_Activity** ────▓▓▓ | PSI: 0.23 (Stable)     | **TP:** 120 | **FP:** 8      |  
| F1-Score: 0.91  ─────     | 2. **Session_Duration** ───▓▓ | Drift Alert: None      | **FN:** 15  | **TN:** 200   |  
| AUC-ROC: 0.98             | 3. **Location** ──────────▓  |                        |                           |  
|---------------------------|-----------------------------|------------------------|---------------------------|  
| **[Prediction Drift]**     | **[Live Inference Stats]**  | **[Resource Usage]**    | **[Alert Log]**            |  
| (Histogram comparison)     | Success: 98%               | CPU: 45%               | **Error:** Model Latency > 200ms |  
|                           | Failed: 2%                 | RAM: 3.2/8GB           |                           |  
+===========================+=============================+========================+===========================+  

---

### **Design Tips for Visual Appeal**  
**Color Coding:**  
- **Suricata:** Red (critical alerts), Orange (high), Yellow (medium), Green (low).  
- **ML:** Blue (metrics), Purple (drift), Green (stable), Red (issues).  

**Layout Tools:**  
- Use **Grafana** (drag-and-drop) for a customizable design.
- **Kibana** (for Suricata + Elasticsearch).
- **Streamlit** (for ML dashboards).

**Icons:**  
- 📍 (geo-location), ⚠️ (warning), ✅ (allowed), ❌ (blocked).

**Dynamic Elements:**  
- Auto-refresh timers (e.g., "Updated 5s ago").
- Sparklines (mini graphs) for traffic or CPU usage.

---

### **Example Network Traffic Panel (Suricata)**  
**[Network Traffic Over Time]**  
───────────────────────────────────────────────  
 12:00 │▓▓▓▓▓▓▓▓▓▓░░  
 12:02 │▓▓▓▓▓▓▓░░░░░  
 12:04 │▓▓▓▓▓▓▓▓▓▓▓▓ (Attack Spike)  
───────────────────────────────────────────────  

---

This mock-up includes all the major components, and you can easily implement this layout using various tools. If you need help with any specific tool setup or further adjustments to the mock-up, feel free to let me know!






## Contact
- Name: Thapelo Mthize
- Email: cyber_shield@icloud.com
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/thapelomthize)

