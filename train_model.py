import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load dataset (replace with your data)
data = pd.read_csv('network_traffic.csv')

# Preprocess
features = data[['src_port', 'dst_port', 'protocol', 'length']]
features = features.fillna(0)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Train Isolation Forest
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(scaled_features)

# Save model
import joblib
joblib.dump(model, 'anomaly_detection_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
