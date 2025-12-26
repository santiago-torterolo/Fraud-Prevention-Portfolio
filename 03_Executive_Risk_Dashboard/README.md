# Executive Risk Dashboard 📊

**Strategic Monitoring of Compliance & Financial Exposure**

This project delivers a high-level command center designed for **C-Level Executives** and **Heads of Compliance**. It moves beyond transactional details to visualize aggregate risk exposure, blockage efficiency, and global fraud hotspots.

### 🚀 [View Live Dashboard on Tableau Public](https://public.tableau.com/views/ExecutiveRiskDashboard/ExecutiveRiskMonitorQ42024?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🎯 Business Objectives

The dashboard answers three critical strategic questions:

1.  **Financial Impact:** What is the total monetary value of fraud prevented by our compliance rules?
2.  **Operational Load:** What is the volume of transactions held for manual review vs. automated blocking?
3.  **Geo-Risk:** Which jurisdictions (e.g., Offshore Zones) are generating the highest risk traffic?

## 📊 Key Performance Indicators (KPIs)

- **Total Fraud Prevented (BAN):** Aggregate EUR value of transactions with `Status = BLOCKED_COMPLIANCE`.
- **Risk Distribution:** Breakdown of traffic into _Approved_, _Manual Review_, and _Blocked_.
- **Regional Exposure:** Heatmap identifying high-value attack vectors by geography.

## 🛠️ Technical Implementation

### 1. Data Simulation Engine

The data is generated via a custom Python script (`src/generate_viz_data.py`) that simulates realistic Q4 financial traffic patterns:

- **Transaction Types:** SWIFT, ACH, WIRE, Internal Transfers.
- **Scenarios:**
  - **"Whales":** High-value transfers from high-risk jurisdictions.
  - **"Structuring":** Multiple small transactions to evade detection.
  - **Compliance Blocks:** Transactions flagged with Risk Scores > 85.

### 2. Visualization (Tableau)

- **Interactive Filters:** Drill-down capabilities by Status and Region.
- **Calculated Fields:** Custom logic to format currency (Millions/Thousands) and segment Risk Scores.
