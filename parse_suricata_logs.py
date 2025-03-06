import json

def read_suricata_alerts(log_file='/var/log/suricata/fast.log'):
    alerts = []
    with open(log_file, 'r') as f:
        for line in f:
            if '[**]' in line:
                parts = line.split('[**]')
                alert = {
                    'timestamp': parts[0].strip(),
                    'signature': parts[1].split('] ')[1].strip(),
                    'severity': 'High'  # Customize based on rules
                }
                alerts.append(alert)
    return alerts

print(read_suricata_alerts())
