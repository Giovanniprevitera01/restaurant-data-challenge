# 🍽️ Restaurant Transactions Analysis

## 📄 Project Overview

This project is part of a data analysis challenge aimed at exploring and extracting insights from a dataset of restaurant transactions. The dataset includes detailed information about sales, products, taxation, and customer behavior.

This challenge was designed to be open-ended to showcase analytical and technical skills in Python, data wrangling, visualization, and reporting.

---

## 📊 Dataset Description

The dataset is composed of three main files:

* `transactions.csv`: Main dataset in CSV format
* `transactions.xlsx`: Same data in Excel format
* `Dataset_notes.pdf`: Explains the fields and structure

Each row likely represents an item sold in a transaction. Multiple rows can have the same `Transaction_ID` if the customer ordered multiple items.

---

## 📚 Project Structure

restaurant-analysis/
├── data/
    └── transactions.csv
    └── transactions.xls
    └── Dataset_notes.pdf
├── notebooks/
│   └── EDA_and_Insights.ipynb
├── report/
│   └── restaurant_report.pdf
├── requirements.txt
├── README.md


---

## 🔧 How to Run the Project

### 1. Clone the Repository
git clone https://github.com/Giovanniprevitera01/restaurant-task.git
cd restaurant-task

### 2. Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Notebook
jupyter notebook notebooks/EDA_and_Insights.ipynb


## 📅 Key Analyses & Visualizations

1. 📈 **Trend delle vendite giornaliere**
2. 🕒 **Distribuzione oraria delle vendite**
3. 💳 **Scontrino medio per cliente**
4. 🧑‍🍳 **Numero medio di ospiti per transazione**
5. 🧵 **Analisi top 10 prodotti più venduti**
6. 💰 **top 10 Prodotti con più incasso**
7. 📋 **Ripartizione vendite per categoria**
8. 📅 **Vendite per giorno della settimana**
9. 📊 **Clustering Clienti (KMeans + PCA)**



📊 Clustering Clienti (KMeans + PCA)

Abbiamo utilizzato KMeans clustering combinato con PCA per ridurre le dimensioni e visualizzare la segmentazione dei clienti. Il risultato ha identificato 4 gruppi principali:

    💸 Cluster 0 – Clienti top spender: spesa elevata, molti ospiti, ampia varietà di prodotti, prevalentemente cena.

    🧍 Cluster 1 – Clienti occasionali: bassa spesa e varietà, visite rapide e poco frequenti.

    🍱 Cluster 2 – Clienti da asporto: acquisti mirati, 100% delle transazioni fuori sede.

    🍽️ Cluster 3 – Clienti “fedeli alla cena”: spesa media, alta incidenza sul servizio serale.
