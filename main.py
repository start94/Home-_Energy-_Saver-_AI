# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import joblib
import pandas as pd
import os

# Carica modello e dati
model_path = os.path.join("models", "rf_energy_model.pkl")
feature_path = os.path.join("models", "feature_cols.pkl")
avg_map_path = os.path.join("models", "avg_map.pkl")

if not all(os.path.exists(p) for p in [model_path, feature_path, avg_map_path]):
    raise FileNotFoundError("File del modello o dati mancanti. Esegui prima 'train_model.py'.")

model = joblib.load(model_path)
feature_cols = joblib.load(feature_path)
avg_map = joblib.load(avg_map_path)

app = FastAPI(
    title="Home Energy Saver AI",
    description="API per la previsione del consumo e suggerimenti energetici"
)

class PredictionRequest(BaseModel):
    device: str
    datetime: datetime

def predict_and_suggest(device: str, when: datetime):
    h = when.hour
    wd = when.weekday()
    is_weekend = 1 if wd >= 5 else 0
    row = {col: 0 for col in feature_cols}
    row.update({
        'Hour': h,
        'Day': when.day,
        'Weekday': wd,
        'Is_Weekend': is_weekend
    })
    dummy_col = f"Device_{device}"
    if dummy_col in row:
        row[dummy_col] = 1
    else:
        return None, f"Dispositivo sconosciuto: {device}"
    
    input_df = pd.DataFrame([row])
    pred = model.predict(input_df)[0]
    avg = avg_map.get((h, device), None)
    
    if avg is None:
        suggestion = "Nessun dato medio disponibile."
    elif pred > avg * 1.10:
        suggestion = f"⚠️ Consumo previsto alto: {pred:.0f}W (media: {avg:.0f}W). Spegnere o posticipare?"
    else:
        suggestion = f"✅ Consumo previsto normale: {pred:.0f}W (media: {avg:.0f}W)."
    
    return pred, suggestion

@app.post("/predict")
def predict(req: PredictionRequest):
    pred, suggestion = predict_and_suggest(req.device, req.datetime)
    if pred is None:
        return {"error": suggestion}
    return {
        "device": req.device,
        "datetime": req.datetime,
        "predicted_consumption": round(pred, 2),
        "suggestion": suggestion
    }