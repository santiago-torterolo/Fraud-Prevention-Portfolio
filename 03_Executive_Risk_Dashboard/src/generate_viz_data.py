


import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

def generate_dashboard_data():
    print("📊 [EXECUTIVE DASHBOARD] Generating strategic risk data...")
    
    # 1. SETUP PATHS
    # Saves to ../data/executive_risk_data.csv
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "../data/executive_risk_data.csv")
    
    # Create data directory if it doesn't exist
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    # 2. CONFIGURATION
    # Simulating Q4 Financial Data
    start_date = datetime(2024, 10, 1)
    n_transactions = 5000
    
    data = []
    
    print("   -> Simulating Q4 Transaction Flow...")

    for _ in range(n_transactions):
        # Random date within the last 90 days
        days_offset = random.randint(0, 90)
        tx_date = start_date + timedelta(days=days_offset)
        
        # Transaction Types (Corporate focus)
        tx_type = random.choice(['WIRE_TRANSFER', 'ACH', 'SWIFT', 'INTERNAL_TRANSFER'])
        
        # EXECUTIVE SCENARIOS
        
        # Scenario A: High Risk / Compliance Block (The "Saves")
        if random.random() < 0.05: # 5% Blocked
            status = 'BLOCKED_COMPLIANCE'
            amount = round(random.uniform(50000, 1000000), 2)
            risk_score = random.randint(85, 99)
            region = random.choice(['High_Risk_Jurisdiction', 'Offshore_Zone'])
        
        # Scenario B: Manual Review Required (Operational Load)
        elif random.random() < 0.10: # 10% For Review
            status = 'MANUAL_REVIEW'
            amount = round(random.uniform(10000, 150000), 2)
            risk_score = random.randint(60, 84)
            region = random.choice(['EU_Non_Member', 'APAC_Emerging'])
            
        # Scenario C: Clean Traffic (Business as Usual)
        else:
            status = 'APPROVED'
            amount = round(random.uniform(100, 50000), 2)
            risk_score = random.randint(1, 20)
            region = random.choice(['EU_Zone', 'North_America', 'Domestic'])

        data.append({
            'Date': tx_date.strftime('%Y-%m-%d'),
            'Transaction_ID': f"TX-{random.randint(100000, 999999)}",
            'Type': tx_type,
            'Amount_EUR': amount,
            'Status': status,
            'Risk_Score': risk_score,
            'Region': region,
            'Analyst_Team': random.choice(['Team_Alpha', 'Team_Beta', 'Auto_System'])
        })

    # 3. EXPORT TO CSV
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    
    print(f"✅ CSV Ready: {output_path}")
    print(f"   Total Volume: €{df['Amount_EUR'].sum():,.2f}")
    print("   Ready for Tableau ingestion.")

if __name__ == "__main__":
    generate_dashboard_data()
