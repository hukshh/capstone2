# 📊 Retail Sales Analysis Dashboard

## 📌 Project Overview
This project analyzes retail sales data to identify trends, high-performing products, customer segments, and regional performance. The goal is to support business decision-making through data-driven insights.

---

## 🎯 Problem Statement
How can sales data be analyzed to identify key revenue drivers, seasonal trends, and areas for business improvement?

---

## 📂 Dataset
* **Source**: Public Superstore Dataset
* **Rows**: 9,800+
* **Columns**: 18
* **Features**: Sales, Category, Segment, Region, Order Date

---

## ⚙️ Workflow

### 1. Data Cleaning (Python)
* Handled missing values (e.g., Postal Codes)
* Converted date formats for time-series analysis
* Standardized column names (lowercase, underscores)
* Created new features (month, year) for granular analysis

### 2. Exploratory Data Analysis
* Analyzed sales trends over time to identify seasonality
* Compared performance across categories and segments
* Evaluated sub-category profitability

### 3. Tableau Dashboard
* Created interactive visualizations for stakeholders
* Developed maps for regional performance tracking
* Built segment-based revenue breakdown charts

---

## 📊 Key Insights
* **Top Category**: Technology is the highest revenue-generating category.
* **Product Leaders**: Phones and Chairs dominate sub-category sales.
* **Segment Breakdown**: The Consumer segment contributes the majority of revenue.
* **Geography**: Sales are heavily concentrated in regions like California and New York.
* **Seasonality**: Trends show peak demand in specific months, suggesting holiday impact.

---

## 💡 Recommendations
* **Inventory Focus**: Prioritize high-performing products like Phones and Chairs.
* **Growth Areas**: Improve marketing for low-performing categories such as Appliances.
* **Expansion**: Target underperforming regions with specific promotional campaigns.
* **B2B Strategy**: Strengthen the Corporate customer segment to diversify revenue streams.

---

## 📁 Repository Structure
```text
capstone-project/
├── data/
│   ├── raw/                   # Original unedited dataset
│   └── processed/             # Cleaned dataset ready for analysis
├── notebooks/
│   ├── 02_cleaning.ipynb      # Data cleaning and preparation
│   ├── 03_eda.ipynb           # Exploratory data analysis
│   └── 04_statistical_analysis.ipynb # Deeper statistical insights
├── tableau/
│   ├── screenshots/           # Dashboard visual exports
│   └── dashboard_links.md     # Links to Tableau Public
├── docs/
│   └── data_dictionary.md     # Column definitions and types
├── reports/
│   └── final_report.md        # Detailed executive summary
├── README.md                  # Project overview (this file)
└── requirements.txt           # Python dependencies
```

---

## 🔗 Links
* **Tableau Dashboard**: [View Live Dashboard](https://public.tableau.com/app/profile/ovais.koite/viz/RetailSalesAnalysis_1714392435/ExecutiveSummary)
* **GitHub Repository**: [Project Repo](https://github.com/ovaiskoite/capstone-project)

---

## 🧠 Tools Used
* **Python**: Pandas, Matplotlib, Seaborn
* **Tableau Public**: Data Visualization & Dashboarding
* **Jupyter**: Interactive Analysis Environment

---

## 👨‍💻 Author
**Ovais Koite**
*Data Analyst*
