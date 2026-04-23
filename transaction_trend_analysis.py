
# Transaction Volume Trend Analysis - Ready to Use Script

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (change path if needed)
df = pd.read_csv('paysim_1000_rows.csv')

# Preview data
print("First 5 rows:")
print(df.head())

# -------------------------------
# 1. Transaction Volume per Step
# -------------------------------
txn_per_step = df.groupby('step').size()

plt.figure()
txn_per_step.plot()
plt.title('Transaction Volume Trend (Step vs Number of Transactions)')
plt.xlabel('Step')
plt.ylabel('Number of Transactions')
plt.show()

# -------------------------------
# 2. Total Amount per Step
# -------------------------------
amount_per_step = df.groupby('step')['amount'].sum()

plt.figure()
amount_per_step.plot()
plt.title('Transaction Amount Trend (Step vs Total Amount)')
plt.xlabel('Step')
plt.ylabel('Total Amount')
plt.show()

# -------------------------------
# 3. Fraud Transactions Trend
# -------------------------------
fraud_trend = df[df['isFraud'] == 1].groupby('step').size()

plt.figure()
fraud_trend.plot()
plt.title('Fraud Transaction Trend')
plt.xlabel('Step')
plt.ylabel('Fraud Count')
plt.show()

# -------------------------------
# 4. Transaction Type Distribution
# -------------------------------
type_count = df['type'].value_counts()

plt.figure()
type_count.plot(kind='bar')
plt.title('Transaction Type Distribution')
plt.xlabel('Transaction Type')
plt.ylabel('Count')
plt.show()

print("\nAnalysis Completed Successfully!")
