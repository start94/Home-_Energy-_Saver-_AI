# Home Energy Saver AI 🏠⚡ENG 
Predict domestic energy consumption and optimize device usage with AI

A REST API built with FastAPI and Random Forest to analyze simulated home energy consumption data and provide real-time suggestions to reduce waste.

🌟 Key Features
AI Prediction : Uses a Random Forest model trained on simulated data to forecast energy usage.
Smart Suggestions : Generates alerts if predicted consumption exceeds historical averages by 10%.
RESTful API : /predict endpoint for structured POST requests with device and timestamp.
Simulated Dataset : Automatically generated data for refrigerators, washing machines, heaters, etc.
📦 Technologies Used
FastAPI
API framework
Random Forest
Machine Learning model
Joblib
Model serialization
Uvicorn
ASGI server
Pandas/Numpy
Data processing

🛠️ Local Setup
# 1. Clone the repository

bash
1 git clone https://github.com/il-tuo-nome/Home_Energy_Saver_AI.git
2 cd Home_Energy_Saver_A

# 2. Create a virtual environment
bash
1 python -m venv venv 
2 source venv/bin/activate  # Linux/macOS
3 venv\Scripts\Activate.ps1  # Windows

# 3. Install dependencies
bash
1 pip install -r requirements.txt

# 4. Train the model (generates dataset and saves the model)
 bash 
 1 python train_model.py

# 5. Start the server
bash
1 uvicorn main:app --reload --port 8000

🌐 API Documentation
The API is accessible via:

Swagger UI : http://127.0.0.1:8000/docs
Redoc : http://127.0.0.1:8000/redoc
Example Request
bash 
POST /predict
{
  "device": "Heater",
  "datetime": "2025-05-03T18:00:00"
}

Response : 
{
  "device": "Heater",
  "datetime": "2025-05-03T18:00:00",
  "predicted_consumption": 1850.0,
  "suggestion": "⚠️ High predicted consumption: 1850W (average: 1600W). Turn off or delay usage?"
}

📈 Simulated Dataset
Data represents hourly energy consumption for 5 household devices:

Refrigerator (100-200W)
Washing Machine (500-1500W)
TV (100-300W)
Laptop (30-90W)
Heater (1000-2000W)
📚 Contribute to the Project
Want to improve the project? You can:

Add new devices to the dataset
Implement a more advanced model (e.g., XGBoost, LSTM)
Create a web dashboard for data visualization
Optimize the API for heavy loads
📄 License
Released under the MIT License .

👤 Contact
GitHub : @start94 - Raffaele Diomaiuto
Email : raffydio1994@gmail.com
✅ Final Notes
The model is trained on simulated data . For real-world use, replace train_model.py with actual historical data.
If you encounter errors like EOFError, run train_model.py first to generate the .pkl files.






# Home Energy Saver AI 🏠⚡ ITALIANO 

Un'API REST per prevedere i consumi energetici domestici e fornire suggerimenti per ridurre gli sprechi.
🌟 Funzionalità Principali
Previsione AI : Usa un modello Random Forest addestrato su dati simulati per prevedere i consumi.
Suggerimenti Smart : Genera avvisi se il consumo previsto supera la media storica del 10%.
API RESTful : Endpoint /predict per richieste POST strutturate con dispositivo e timestamp.
Dati Simulati : Dataset generato automaticamente per frigoriferi, lavatrici, riscaldamenti, ecc.

## 📦 Tecnologie Utilizzate
- **FastAPI**: Framework per l'API REST
- **Random Forest**: Modello ML per le previsioni
- **Joblib**: Per il salvataggio del modello
- **Uvicorn**: Server ASGI

🛠️ Setup Locale
1. Clona il repository:
   ```bash
   git clone https://github.com/il-tuo-nome/Home_Energy_Saver_AI.git
   cd Home_Energy_Saver_AI

2. Crea l'ambiente virtuale
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\Activate.ps1  # Windows

3. Installa le dipendenze
pip install -r requirements.txt

4. Addestra il modello (genera dataset e salva il modello)
python train_model.py

5. Avvia il server
uvicorn main:app --reload --port 8000

🌐 API Documentation
L'API è accessibile tramite:

Swagger UI : http://127.0.0.1:8000/docs
Redoc : http://127.0.0.1:8000/redoc


Esempio di richiesta :
POST /predict
{
  "device": "Heater",
  "datetime": "2025-05-03T18:00:00"
}

Risposta:
{
  "device": "Heater",
  "datetime": "2025-05-03T18:00:00",
  "predicted_consumption": 1850.0,
  "suggestion": "⚠️ Consumo previsto alto: 1850W (media: 1600W). Spegnere o posticipare?"
}

📈 Dataset Simulato
I dati rappresentano consumi energetici orari per 5 dispositivi domestici:

Frigorifero (100-200W)
Lavatrice (500-1500W)
TV (100-300W)
Laptop (30-90W)
Riscaldamento (1000-2000W)


📚 Contribuire al Progetto
Vuoi migliorare il progetto? Puoi:

Aggiungere nuovi dispositivi al dataset
Implementare un modello più avanzato (es. XGBoost, LSTM)
Creare una dashboard web per visualizzare i dati
Ottimizzare l'API per carichi pesanti
📄 Licenza
Progetto rilasciato sotto MIT License .

👤 Contatto
GitHub : @start94   Raffaele Diomaiuto
Email : raffydio1994@gmail.com
