# train_model.py
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

# 1) Generazione del dataset simulato
devices = {
    "Fridge": (100, 200),
    "Washing machine": (500, 1500),
    "TV": (100, 300),
    "Laptop": (30, 90),
    "Heater": (1000, 2000)
}

start_date = datetime(2025, 4, 22, 0, 0)
end_date = datetime(2025, 4, 29, 0, 0)
interval = timedelta(hours=1)
timestamps = []
t = start_date
while t < end_date:
    timestamps.append(t)
    t += interval

data = []
for ts in timestamps:
    for dev, (low, high) in devices.items():
        data.append([ts, dev, np.random.randint(low, high)])

df = pd.DataFrame(data, columns=['Timestamp', 'Device', 'Power_Consumption_Watt'])
os.makedirs("data", exist_ok=True)
df.to_csv('data/energy_consumption_simulated.csv', index=False)
print("✅ Dataset simulato creato:", df.shape)

# 2) Preprocessing
df = pd.read_csv('data/energy_consumption_simulated.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.day
df['Weekday'] = df['Timestamp'].dt.weekday
df['Is_Weekend'] = df['Weekday'].apply(lambda x: 1 if x >= 5 else 0)
df = pd.get_dummies(df, columns=['Device'])
df['Power_Normalized'] = MinMaxScaler().fit_transform(df[['Power_Consumption_Watt']])
df.to_csv('data/processed_energy_data.csv', index=False)
print("✅ Preprocessing completato:", df.shape)

# 3) Addestramento
X = df.drop(columns=['Timestamp', 'Power_Consumption_Watt', 'Power_Normalized'])
y = df['Power_Consumption_Watt']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4) Salvataggio
os.makedirs("models", exist_ok=True)
joblib.dump(model, 'models/rf_energy_model.pkl')
joblib.dump(X_train.columns.tolist(), 'models/feature_cols.pkl')

# 5) Calcolo consumi medi storici
df_raw = pd.read_csv('data/energy_consumption_simulated.csv')
df_raw['Timestamp'] = pd.to_datetime(df_raw['Timestamp'])
df_raw['Hour'] = df_raw['Timestamp'].dt.hour
avg_map = df_raw.groupby(['Hour', 'Device'])['Power_Consumption_Watt'].mean().to_dict()
joblib.dump(avg_map, 'models/avg_map.pkl')

print("✅ Modello e dati salvati in 'models/'")