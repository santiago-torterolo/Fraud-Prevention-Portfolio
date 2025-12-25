# SQL Fraud Audit: Post-Transaction Monitoring ⚖️

This project implements a **Rule-Based Audit System** using SQL to detect fraud patterns that often bypass real-time filters. It focuses on identifying **Structuring (Smurfing)** and **Velocity Abuse**.

### 📂 Dataset Information: PaySim Schema

This project is built upon the schema of the **[PaySim Mobile Money Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)**, a synthetic dataset generated from real log analysis.

> **Note on Data Usage:**
> The full PaySim dataset contains **~6 million rows (250MB+)**, which exceeds GitHub's file size limits and is impractical for a portable demo portfolio.
>
> Instead of requiring external downloads, this repository includes a **Data Simulation Engine** (`src/setup_audit_db.py`) that:
>
> 1.  Replicates the exact PaySim schema (`step`, `type`, `amount`, `nameOrig`, etc.).
> 2.  Injects specific fraud scenarios (Structuring, Bot Attacks) for validation.
> 3.  Generates a lightweight SQLite database locally for immediate testing.

### 🕵️‍♂️ Audit Logic (SQL)

The system executes the following checks against the `paysim_transactions` table:

#### 1. Structuring Detection (Smurfing)

- **Objective:** Identify users evading the $10,000 reporting threshold.
- **Logic:** Filter for `CASH_OUT` transactions between **$9,000 and $9,999**. Group by user to find repeated attempts.
  ```
  SELECT nameOrig, COUNT(*) ...
  WHERE amount BETWEEN 9000 AND 9999
  GROUP BY nameOrig HAVING COUNT(*) >= 3
  ```

#### 2. Velocity Abuse (Bot/Scripting)

- **Objective:** Detect automated scripts draining accounts or testing cards.
- **Logic:** Count transactions per user per time-step (1 hour). Alert if **> 15 TXs/hour**.
  ```
  SELECT nameOrig, step, COUNT(*) ...
  GROUP BY nameOrig, step HAVING COUNT(*) > 15
  ```

### 🚀 How to Run

1.  **Generate the Database:**

    ```
    python src/setup_audit_db.py
    ```

    _(Creates `data/paysim_audit.db`)_

2.  **Run the Audit:**
    ```
    python src/run_audit.py
    ```
    _(Executes SQL queries and prints tables of flagged users)_
