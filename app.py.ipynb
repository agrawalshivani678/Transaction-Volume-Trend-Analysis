{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57d432ff-ca72-42d3-952a-b4d5b580b68c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "st.title(\"📊 Transaction Volume Trend Analysis\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload your PaySim Dataset\", type=[\"csv\"])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    df = pd.read_csv(uploaded_file)\n",
    "\n",
    "    st.subheader(\"📌 Dataset Preview\")\n",
    "    st.write(df.head())\n",
    "\n",
    "    st.subheader(\"📈 Transaction Volume Trend\")\n",
    "    txn_per_step = df.groupby('step').size()\n",
    "\n",
    "    fig1, ax1 = plt.subplots()\n",
    "    ax1.plot(txn_per_step)\n",
    "    ax1.set_xlabel(\"Step\")\n",
    "    ax1.set_ylabel(\"Number of Transactions\")\n",
    "    st.pyplot(fig1)\n",
    "\n",
    "    st.subheader(\"💰 Transaction Amount Trend\")\n",
    "    amount_per_step = df.groupby('step')['amount'].sum()\n",
    "\n",
    "    fig2, ax2 = plt.subplots()\n",
    "    ax2.plot(amount_per_step)\n",
    "    ax2.set_xlabel(\"Step\")\n",
    "    ax2.set_ylabel(\"Total Amount\")\n",
    "    st.pyplot(fig2)\n",
    "\n",
    "    st.subheader(\"🚨 Fraud Trend\")\n",
    "    fraud_trend = df[df['isFraud'] == 1].groupby('step').size()\n",
    "\n",
    "    fig3, ax3 = plt.subplots()\n",
    "    ax3.plot(fraud_trend)\n",
    "    ax3.set_xlabel(\"Step\")\n",
    "    ax3.set_ylabel(\"Fraud Count\")\n",
    "    st.pyplot(fig3)\n",
    "    \n",
    "    st.subheader(\"📊 Transaction Type Distribution\")\n",
    "    type_count = df['type'].value_counts()\n",
    "\n",
    "    fig4, ax4 = plt.subplots()\n",
    "    type_count.plot(kind='bar', ax=ax4)\n",
    "    ax4.set_xlabel(\"Transaction Type\")\n",
    "    ax4.set_ylabel(\"Count\")\n",
    "    st.pyplot(fig4)\n",
    "\n",
    "else:\n",
    "    st.warning(\"Please upload a dataset to proceed.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
