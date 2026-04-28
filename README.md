# 🛒 E-commerce Sales Analysis Capstone Project

## 🎯 Problem Statement
In the competitive e-commerce landscape, understanding sales trends and customer behavior is crucial. This project addresses the need for clear, data-driven insights to optimize sales strategies, manage inventory efficiently, and identify high-growth opportunities.

## 📊 Dataset Description
The dataset used in this project contains transaction-level sales data, including:
- **Order Details**: Dates, IDs, and shipping modes.
- **Customer Info**: Names, segments, and geographical locations.
- **Product Info**: Categories, sub-categories, and specific product names.
- **Financials**: Sales figures for each transaction.

## 🛠️ Tools Used
- **Python**: Primary language for data processing.
- **Pandas**: Used for data cleaning, transformation, and normalization.
- **Tableau**: Used for creating interactive dashboards and final visualizations.

## 🔄 Project Workflow
1. **Data Loading**: Importing raw CSV data into a Python environment.
2. **Data Cleaning**: Handling missing values (e.g., Postal Codes) and normalizing column names.
3. **Date Processing**: Converting strings to datetime objects and extracting months/years.
4. **Data Export**: Saving the cleaned dataset as `cleaned_data.csv`.
5. **Visualization**: Importing cleaned data into Tableau for final dashboarding.

## 📁 Project Structure
```text
capstone-project/
├── data/              # Raw and cleaned data files
├── notebooks/         # Python scripts for data processing
├── dashboard/         # Tableau workbook and visualizations
├── reports/           # Documentation and insights reports
├── README.md          # Project overview (this file)
└── requirements.txt   # Python dependencies
```

## 🔍 Key Insights
- **Seasonality**: Sales peak during specific months, indicating a need for seasonal marketing.
- **Categories**: The "Technology" category often leads in revenue, while "Office Supplies" leads in volume.
- **Efficiency**: Standard shipping is the most common mode, but Second Class shows higher growth.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the cleaning script: `python3 notebooks/analysis.py`
3. View the results in `data/cleaned_data.csv` and `reports/insights.md`
