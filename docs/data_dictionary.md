# 📖 Data Dictionary

This document describes the columns available in the retail sales dataset used for this project.

| Column Name | Description | Data Type | Example Value |
| :--- | :--- | :--- | :--- |
| `order_id` | Unique identifier for each sales transaction. | String | CA-2023-152156 |
| `order_date` | The date the order was placed. | Datetime | 2023-11-08 |
| `ship_mode` | The shipping method chosen for the order. | String | Second Class |
| `customer_name`| Name of the customer who placed the order. | String | Claire Gute |
| `segment` | The market segment the customer belongs to. | String | Consumer |
| `country` | Country where the order was placed. | String | United States |
| `city` | City where the order was placed. | String | Henderson |
| `state` | State where the order was placed. | String | Kentucky |
| `postal_code` | Postal code of the delivery location. | Integer | 42420 |
| `region` | Geographical region of the sale. | String | South |
| `product_id` | Unique identifier for the product. | String | FUR-BO-10001798 |
| `category` | High-level category of the product. | String | Furniture |
| `sub_category` | Detailed sub-category of the product. | String | Bookcases |
| `product_name` | Name of the specific product. | String | Bush Somerset Bookcase |
| `sales` | Total revenue generated from the sale. | Float | 261.96 |
| `quantity` | Number of items sold. | Integer | 2 |
| `discount` | Discount applied to the sale (as a decimal). | Float | 0.0 |
| `profit` | Net profit generated from the sale. | Float | 41.91 |
| `month` | Month extracted from the order date. | Integer | 11 |
| `year` | Year extracted from the order date. | Integer | 2023 |
