import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Transaction Volume Trend Analysis")

uploaded_file = st.file_uploader("Upload your PaySim Dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.write(df.head())

    st.subheader("📈 Transaction Volume Trend")
    txn_per_step = df.groupby('step').size()

    fig1, ax1 = plt.subplots()
    ax1.plot(txn_per_step)
    ax1.set_xlabel("Step")
    ax1.set_ylabel("Number of Transactions")
    st.pyplot(fig1)

    st.subheader("💰 Transaction Amount Trend")
    amount_per_step = df.groupby('step')['amount'].sum()

    fig2, ax2 = plt.subplots()
    ax2.plot(amount_per_step)
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Total Amount")
    st.pyplot(fig2)

    st.subheader("🚨 Fraud Trend")
    fraud_trend = df[df['isFraud'] == 1].groupby('step').size()

    fig3, ax3 = plt.subplots()
    ax3.plot(fraud_trend)
    ax3.set_xlabel("Step")
    ax3.set_ylabel("Fraud Count")
    st.pyplot(fig3)

    st.subheader("📊 Transaction Type Distribution")
    type_count = df['type'].value_counts()

    fig4, ax4 = plt.subplots()
    type_count.plot(kind='bar', ax=ax4)
    ax4.set_xlabel("Transaction Type")
    ax4.set_ylabel("Count")
    st.pyplot(fig4)

else:
    st.warning("Please upload a dataset to proceed.")
