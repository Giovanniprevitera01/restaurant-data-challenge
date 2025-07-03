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
├── app.py
├── README.md


---

## 🔧 How to Run the Project

### 1. Clone the Repository
git clone https://github.com/Giovanniprevitera01/restaurant-data-challenge.git
cd restaurant-data-challenge

### 2. Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate 

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Notebook
jupyter notebook

### 5. Run the dashboard
cd restaurant-analitycs
pip install dash pandas plotly
python app.py
Vai su http://127.0.0.1:8050 per vedere la dashboard.


## 📅 Key Analyses & Visualizations

    📈 Daily Sales Trends

    🕒 Hourly Sales Distribution

    💳 Average Ticket per Customer

    🧑‍🍳 Average Number of Guests per Transaction

    🧵 Top 10 Best-Selling Products

    💰 Top 10 Products by Revenue

    📋 Sales Breakdown by Category

    📅 Sales by Day of the Week

    📊 Customer Clustering (KMeans + PCA)



## 🚀 Dashboard Features

    📅 Date range filters

    🍽️ Product category filter

    🚚 Order type filter: Dine-in / Takeaway-Delivery

    📈 Dynamic KPIs: Total Sales, Average Ticket, Number of Transactions

## 📊 Interactive Graphs

        1.Daily Sales Trend

        2.Top 10 Best-Selling Products (with names)

        3.Sales by Day of the Week

        4.Hourly Heatmap of Sales by Day

## 📊 Customer Clustering (KMeans + PCA)

We applied KMeans clustering combined with PCA for dimensionality reduction to visualize customer segmentation. This analysis identified 4 main customer groups:

    💸 Cluster 0 – High Spenders: Large total spend, high number of guests, wide variety of products, primarily dinner service.

    🧍 Cluster 1 – Occasional Customers: Low spend and variety, quick and infrequent visits.

    🍱 Cluster 2 – Takeaway Customers: Focused purchases, 100% of transactions for off-premises consumption.

    🍽️ Cluster 3 – Loyal Dinner Guests: Medium spend, high incidence of dinner service.
