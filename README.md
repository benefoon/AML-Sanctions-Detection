## 🛡️ AML & Sanctions Detection Platform

A production-grade platform for detecting **money laundering activities** and **sanctioned entity transactions** using advanced **machine learning**, **deep learning**, and **graph-based techniques**.
This system is designed to be **modular**, **secure**, and **scalable**, capable of processing large volumes of data from banking, fintech, and regulatory systems.

---

### 🚀 Features

* ✅ **Multi-layer Name Matching** with Fuzzy Logic & Semantic Similarity
* 📊 **Explainability** with SHAP analysis for model interpretability
* 🔒 **Enterprise-grade Security** (token auth, IP anomaly detection, AES encryption)
* 🧠 **Deep Learning + Ensemble Models** for fraud and sanction risk scoring
* 🕸️ **Graph-based Linking** for hidden relationship discovery
* ⚙️ **Preprocessing Pipelines** (scikit-learn compatible)
* 🔬 **Modular Inference System** with multiple APIs
* 🧪 **Integrated Unit Testing** with `pytest`

---

### 📁 Project Structure

```
├── api/                  # FastAPI endpoints (e.g., /predict)
├── core/                 # Security, monitoring, and core logic
├── data/                 # Sanctions list loaders and utilities
├── deep_models/          # Deep neural network models & utils
├── explainability/       # SHAP and model interpretability
├── features/             # Preprocessing feature pipelines
├── graph/                # Relationship graphs & entity linking
├── inference/            # Prediction logic for runtime
├── models/               # Ensemble and base ML models
├── preprocessing/        # Matching, cleaning, and text parsing
├── sanctions/            # Official matching logic
├── semantic_name_matching/  # BERT/Transformer-based name analysis
├── src/                  # Internal utilities
├── tests/                # Unit + integration tests (pytest)
├── training/             # Model training scripts
├── utils/                # Logging, config, utilities
├── config.py             # Central configuration file
├── README.md             # Documentation
```

---

### 🔍 Core Modules

| Module              | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `ip_analyzer.py`    | Detects suspicious IP patterns and bans high-frequency actors.   |
| `token_auth.py`     | Token-based API security with rotation support.                  |
| `encryption.py`     | AES-GCM encryption for sensitive fields (PII masking).           |
| `ensemble_model.py` | Combines multiple classifiers for robust fraud prediction.       |
| `shap_analysis.py`  | Visual & numerical feature attribution for model transparency.   |
| `fuzzy_match.py`    | Handles typographical & phonetic variations in names.            |
| `matching.py`       | Matches user records against updated OFAC/EU/UN sanctions lists. |

---

### 🛠️ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/your-org/aml-sanctions-detection.git
cd aml-sanctions-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
pytest tests/

# 4. Launch API (FastAPI)
uvicorn api.predict:app --reload
```

---
### 🧪 Example Inference

```bash
POST /predict
{
  "sender_name": "Ali Hosseini",
  "receiver_name": "Alexander Ivanov",
  "country": "Russia",
  "amount": 15000
}
→ Response: { "risk_score": 0.87, "sanction_match": true }
```

---

### 📌 Security

* ✅ **API Token Authentication** with optional JWT rotation
* 🔐 **AES-256 GCM Encryption** of sensitive fields
* 🛡️ **IP Anomaly Monitoring** to detect brute-force access
* 🔍 **Redaction Engine** to mask names in logs

---

### 📈 Model Training

```bash
python training/train_model.py
```

Supports:

* `XGBoost`
* `LightGBM`
* `RandomForest`
* Deep Learning architectures (LSTM, DNN)
