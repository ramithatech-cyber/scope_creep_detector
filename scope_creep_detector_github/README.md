# 🚀 Scope Creep Detector

An AI-powered web application to detect and analyze **scope creep** in software projects — built with Streamlit and scikit-learn.

> **SEPM Mini Project** | Software Engineering & Project Management

---

## 📌 What is Scope Creep?

Scope creep occurs when new features or requirements are added to a project beyond the originally agreed-upon scope — often without adjusting timelines or budgets. This tool helps project managers identify and quantify that risk early.

---

## ✨ Features

- **Scope Creep Detection** — Compares new features against the initial scope using TF-IDF + Cosine Similarity
- **Impact Analysis** — Estimates additional time (days) and cost (₹) for each out-of-scope feature
- **Risk Classification** — Categorizes risk as Low / Medium / High with a numeric risk score
- **Recommendations** — Actionable advice for the project manager
- **Visual Dashboard** — Bar chart visualization of impact metrics

---

## 🛠 Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Frontend     | Streamlit                         |
| ML / NLP     | scikit-learn (TF-IDF, Cosine Sim) |
| Visualization| Matplotlib                        |
| Language     | Python 3.10+                      |

---

## 📂 Project Structure

```
scope_creep_detector/
├── .streamlit/
│   └── config.toml        # Dark theme configuration
├── app.py                 # Main Streamlit application
├── scope_detector.py      # TF-IDF based scope creep detection logic
├── impact_analyzer.py     # Time, cost & risk impact estimation
├── recommendation.py      # Project management recommendations
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/scope_creep_detector.git
cd scope_creep_detector
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🖥️ How to Use

1. Enter your **Initial Features** (comma-separated), e.g. `login, dashboard, reports`
2. Enter the **New Features** being requested, e.g. `chatbot, analytics, AI assistant`
3. Click **Analyze Scope Impact**
4. View the risk score, KPI cards, health indicator, and chart

---

## 📊 How Detection Works

Each new feature is compared against the original scope using **TF-IDF vectorization** and **cosine similarity**:
- **Similarity ≥ 0.5** → Feature is within scope (not flagged)
- **Similarity < 0.5** → Feature is out of scope (scope creep)

Impact is then calculated:
- **+3 days** and **₹10,000** per out-of-scope feature
- Risk Score: Low (30%) · Medium (60%) · High (90%)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is for educational purposes under the SEPM course.
