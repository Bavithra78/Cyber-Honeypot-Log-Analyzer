# 🛡️ Honeypot Threat Monitoring Dashboard

A beginner-friendly cybersecurity analytics project that visualizes **synthetic honeypot logs** using Streamlit.

## 📌 Project Overview

Honeypots are decoy systems designed to attract suspicious activity and collect security-related information. This project provides a simple dashboard to analyse those events.

The dashboard displays:
- Total security events
- Critical events
- Unique source IP addresses
- Blocked or redirected events
- Threat severity distribution
- Threat type distribution
- Protocol usage
- Filterable event logs

> **Note:** The included dataset is synthetic and is intended only for educational/demo purposes.

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- CSV

## 📂 Project Structure

```text
Cyber_Honeypot_Log_Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│   └── honeypot_logs.csv
└── screenshots/
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd Cyber_Honeypot_Log_Analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📊 Example Insights

The dashboard can help identify:
- Frequently observed attack types
- High and critical severity events
- Commonly targeted protocols
- Source IP activity
- Security actions such as monitoring, blocking and redirection

## 🚀 Future Enhancements

- Real-time log ingestion
- AI-based threat classification
- Attacker fingerprinting
- Automated alert generation
- Integration with a real honeypot such as Cowrie
- Time-series attack analysis

## 👩‍💻 Author

Bavithra Bavi
