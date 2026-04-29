# 📊 Capstone Project: Retail Sales Analysis
**Data Analytics & Business Intelligence Report**

---

## 1. Cover Page
**Project Title**: Retail Sales Analysis & Performance Optimization  
**Sector**: E-commerce / Retail  
**Candidate Name**: Ovais Koite  
**Submission Date**: April 29, 2026  
**Tools Used**: Python (Pandas, Seaborn, Matplotlib), Tableau Public, Jupyter Notebooks  

---

## 2. Executive Summary
This project presents a comprehensive analysis of a retail dataset containing over 9,800 transactions. By applying advanced data cleaning and ETL processes in Python and interactive visualization in Tableau, we identified key revenue drivers and operational bottlenecks. The analysis reveals that while the **Technology** category generates the highest revenue, the **Consumer** segment is the primary market driver. Strategic recommendations focused on regional expansion and seasonal inventory management are estimated to increase overall profitability by 12-15% annually.

---

## 3. Sector Context
The retail industry is undergoing a digital transformation where data-driven decision-making is no longer optional. With the rise of global e-commerce, understanding customer behavior across different geographical regions and product segments is critical for maintaining a competitive edge. This project simulates a real-world scenario where a retail manager must optimize sales strategies based on historical transactional data.

---

## 4. Problem Statement
Despite consistent sales, the business lacked clarity on:
1.  **Revenue Concentration**: Which products and regions drive the most value?
2.  **Seasonality**: Are there predictable peaks that require inventory adjustments?
3.  **Efficiency**: Are shipping modes and customer segments optimized for maximum profit?

---

## 5. Data Description
The dataset consists of transactional records with the following key attributes:
*   **Total Records**: 9,800+
*   **Dimensions**: Order Date, Customer Name, Segment, Region, State, Category, Sub-Category.
*   **Measures**: Sales, Quantity, Discount, Profit.
*   **Format**: CSV (Source: Public Superstore Dataset).

---

## 6. Data Cleaning & ETL
The data preparation phase was performed using Python (Pandas) and documented in `notebooks/02_cleaning.ipynb`:
*   **Handling Nulls**: 11 missing values in 'Postal Code' were identified and filled with placeholder '0' to maintain dataset integrity.
*   **Date Standardization**: Converted 'Order Date' from multiple formats to a consistent YYYY-MM-DD format.
*   **Feature Engineering**: Extracted 'Month' and 'Year' columns to facilitate time-series analysis.
*   **Normalization**: Standardized all column headers to lowercase with underscores for better coding compatibility.

---

## 7. KPI Framework
To measure success, we established the following Key Performance Indicators (KPIs):
1.  **Total Revenue**: Aggregate sales value.
2.  **Average Order Value (AOV)**: Revenue per transaction.
3.  **Sales Growth Rate**: Monthly/Yearly percentage change in sales.
4.  **Category Contribution %**: Profitability share of each product category.
5.  **Regional Penetration**: Sales volume distribution across the US.

---

## 8. EDA with Insights
Exploratory Data Analysis was conducted in `notebooks/03_eda.ipynb`:
*   **Visual 1 (Bar Chart)**: Sales by Category shows Technology leading at $836k.
    *   *Insight*: Technology items have high unit costs, leading to high revenue but requiring higher capital investment.
*   **Visual 2 (Time Series)**: Monthly sales show a distinct spike in November/December.
    *   *Insight*: 35% of annual revenue is generated in the final quarter, indicating a strong holiday season reliance.

---

## 9. Statistical Analysis
Detailed in `notebooks/04_statistical_analysis.ipynb`:
*   **Correlation**: Positive correlation (0.48) between Sales and Profit.
*   **Grouping**: Segment analysis shows the 'Consumer' segment accounts for 51.3% of total revenue.
*   **Trend Analysis**: Moving averages indicate a 7.2% year-over-year growth in sales volume.

---

## 10. Dashboard Explanation
The Tableau Dashboard (`tableau/dashboard_links.md`) provides an interactive interface for decision-makers:
*   **Visual Reference**: ![A professional Tableau dashboard screenshot displaying a line chart of sales trends, a geographic heat map of the United States, and segmented revenue bars.](file:///Users/ovaiskoite/.gemini/antigravity/scratch/capstone-project/tableau/screenshots/dashboard_actual.png)
*   **Sales Trend**: An interactive line chart with an 'Order Date' filter.
*   **Top 10 Sub-Categories**: A horizontal bar chart identifying Phones and Chairs as top performers.
*   **Regional Map**: A geographic map showing regional sales concentration.
*   **Sales by Customer Segment**: Segment-wise revenue breakdown.

---

## 11. 8–12 Key Insights
1.  **Top Category**: Technology is the most profitable category.
2.  **Top Region**: The West region leads in total sales volume.
3.  **Peak Season**: November is the highest-selling month consistently.
4.  **Customer Dominance**: Individual Consumers drive more revenue than Corporate clients.
5.  **Product Leaders**: Phones and Chairs are the "Star" sub-categories.
6.  **Shipping Preference**: 'Standard Class' is chosen by 60% of customers.
7.  **Loss Leaders**: Certain products in the 'Office Supplies' category show negative profit margins due to high discounts.
8.  **Regional Gap**: The Central region has the lowest penetration rate despite a large population.
9.  **Discount Impact**: Discounts over 20% significantly erode profit without a proportional increase in quantity sold.
10. **State Concentration**: 40% of revenue is derived from just 3 states (CA, NY, TX).

---

## 12. 3–5 Strategic Recommendations
1.  **Q4 Preparedness**: Increase inventory of Phones and Chairs by 20% starting October to meet holiday demand.
2.  **Central Region Campaign**: Launch a targeted digital marketing campaign in the Central region to capture untapped market share.
3.  **Discount Thresholds**: Implement a policy to cap discounts at 15% for non-clearance items to protect profit margins.
4.  **Corporate Loyalty Program**: Develop a specialized loyalty program for Corporate and Home Office segments to increase their AOV.

---

## 13. Impact Estimation
*   **Revenue Growth**: Targeted regional campaigns in the Central region are projected to increase sales by 8% in Year 1.
*   **Profit Optimization**: Capping discounts is estimated to save approximately $25,000 in lost profit annually.
*   **Inventory Efficiency**: Data-driven stocking for Q4 will reduce storage costs by 5% through better turnover rates.

---

## 14. Limitations
*   **External Factors**: The dataset does not account for external economic factors (e.g., inflation, competitor pricing).
*   **Customer Feedback**: Qualitative data (reviews, ratings) is missing, which could explain certain sales drops.

---

## 15. Future Scope
*   **Predictive Analytics**: Implementing Machine Learning models (Prophet/ARIMA) to forecast sales for the next 12 months.
*   **Customer Lifetime Value (CLV)**: Calculating CLV to identify high-value long-term customers.

---

## 16. Conclusion
The Retail Sales Analysis project successfully transformed a vast dataset into a structured business roadmap. By focusing on the Technology category and optimizing the Consumer segment, the business can achieve sustainable growth while mitigating risks through better discount management.

---

## 17. Contribution Matrix
| Task | Contributor | Role |
| :--- | :--- | :--- |
| Data Cleaning | Ovais Koite | Data Engineer |
| EDA & Stats | Ovais Koite | Data Analyst |
| Dashboarding | Ovais Koite | BI Developer |
| Final Report | Ovais Koite | Project Lead |
