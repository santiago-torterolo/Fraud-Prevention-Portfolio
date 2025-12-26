# Executive Risk Dashboard 📊

**Strategic Monitoring of Compliance & Financial Exposure**

This project delivers a high-level command center designed for **C-Level Executives** and **Heads of Compliance**. It moves beyond simple transactional lists to visualize aggregate risk exposure, analyst team efficiency, and critical anomaly detection.

### 🚀 [View Live Dashboard on Tableau Public](https://public.tableau.com/views/ExecutiveRiskDashboard/ExecutiveRiskMonitorQ42024?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🎯 Business Objectives

The dashboard is engineered to answer three critical strategic questions in real-time:

1.  **Financial Impact:** What is the total monetary value of fraud prevented ("saved") versus the total exposure currently under review?
2.  **Operational Efficiency:** How are the different analyst teams (Auto_System vs. Human Teams) performing in terms of volume and risk detection?
3.  **Anomaly Detection:** Which specific high-value transactions present a critical risk score (outliers) requiring immediate executive intervention?

## 📊 Key Performance Indicators (KPIs) & Visuals

The dashboard is structured into three logical layers:

- **Executive Header (KPIs):**

  - **Total Exposure:** Real-time sum of all transaction volumes (EUR).
  - **Global Risk Score:** Weighted average risk score across the portfolio.
  - **Fraud Prevented:** Aggregate value of blocked transactions (Money Saved).

- **Trend & Performance Layer:**

  - **Temporal Analysis:** Area chart visualization showing the daily volume of Approved vs. Blocked transactions to detect attack spikes.
  - **Analyst Efficiency:** Comparative breakdown of `Auto_System`, `Team_Alpha`, and `Team_Beta` workloads and their respective blockage rates.

- **Risk Matrix (Deep Dive):**
  - **Scatter Plot Analysis:** A specialized view correlating `Amount_EUR` vs. `Risk_Score`. This visual instantly highlights "Black Swans" (High Value + High Risk) that standard reports often miss.

## 🛠️ Technical Implementation

### 1. Data Simulation Engine

The data is generated via a custom Python script that simulates realistic Q4 financial traffic patterns:

- **Transaction Types:** SWIFT, ACH, WIRE, Internal Transfers.
- **Scenarios Modeled:**
  - **"Whales":** High-value transfers from high-risk jurisdictions.
  - **"Structuring":** Multiple small transactions designed to evade detection.
  - **Compliance Blocks:** Automatic flags for transactions with Risk Scores > 85.

### 2. Tableau Architecture

- **LOD Expressions:** Used for calculating regional averages without breaking the transaction-level detail.
- **Interactive Actions:** Implemented dashboard actions where selecting a specific Analyst Team filters the Risk Matrix to show only their relevant cases.
- **Custom Calculated Fields:**
  - `Risk_Category`: Dynamic segmentation (Critical/High/Medium/Low) based on score thresholds.
  - `Compliance_Rate`: Efficiency metric for team performance.

---

## 📂 Project Structure

03_Executive_Risk_Dashboard/
├── data/
│ ├── executive_risk_data.csv # The primary dataset used for the dashboard
│ └── dictionary.md # Data dictionary explaining columns (Status, Type, etc.)
├── src/
│ ├── generate_viz_data.py # Python script for synthetic data generation
│ └── data_cleaning.ipynb # Notebook for pre-processing and validation
├── assets/
│ ├── dashboard_preview.png # Screenshot of the final dashboard
│ └── logical_diagram.png # Architecture of the risk model
├── Tableau/
│ └── Executive_Risk_Workbook.twbx # Local backup of the Tableau workbook
└── README.md # Project documentation

---

## 📬 Contact & Feedback

This dashboard is part of a broader **Fraud Prevention Project**. If you have questions about the risk logic or the data generation process, feel free to reach out.

**Santiago Torterolo**
[LinkedIn Profile](https://linkedin.com/in/santiago-torterolo-5u)
