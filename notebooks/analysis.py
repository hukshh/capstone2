# analysis.py
# This script is for exploring our e-commerce sales data to understand its structure.

import pandas as pd

# --- Step 1: Load the Dataset ---
# We use the relative path '../data/raw_data.csv' because the script is inside the 'notebooks/' 
# folder and needs to go up one level ('..') to find the 'data/' folder.
try:
    # Load the data into a DataFrame (a table-like structure in pandas)
    df = pd.read_csv('data/raw_data.csv')
    
    print("✅ Data loaded successfully!")
    
    # --- Step 2: Dataset Preview ---
    # Display the first 10 rows to see what the data looks like
    print("\n--- First 10 rows of the dataset ---")
    print(df.head(10))

    # --- Step 3: Dataset Exploration ---
    # Print the shape (number of rows and columns)
    print("\n--- Dataset Shape (Rows, Columns) ---")
    print(df.shape)

    # Print the column names as a list
    print("\n--- Column Names ---")
    print(df.columns.tolist())

    # Print the data type of each column
    print("\n--- Column Data Types ---")
    print(df.dtypes)
    # --- Step 4: Data Quality Checks ---
    # It is important to check if our data is clean before we analyze it.

    # Check for missing values in each column
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Check for any rows that are exact duplicates
    print("\n--- Duplicate Rows ---")
    print(df.duplicated().sum())

    # Show statistical summary for numerical columns (Mean, Max, Min, etc.)
    print("\n--- Basic Statistics ---")
    print(df.describe())
    # --- Step 5: Date Processing ---
    # We process dates so we can analyze sales trends over time (monthly, yearly, etc.)

    # Check if 'Order Date' exists; if not, we create it for our analysis
    if 'Order Date' in df.columns:
        print("\n✅ 'Order Date' column found. Converting to datetime...")
        
        # Dataset contains mixed date formats, so we use format='mixed' with dayfirst=True
        df['order_date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)
    else:
        print("\n⚠️ 'Order Date' not found. Generating random dates for analysis...")
        # Fallback: Create random dates between 2022 and 2023
        start_date = pd.to_datetime('2022-01-01')
        end_date = pd.to_datetime('2023-12-31')
        date_range = pd.date_range(start=start_date, end=end_date)
        df['order_date'] = pd.Series(date_range).sample(n=len(df), replace=True).values

    # Extract the month and year into new columns for easier grouping
    df['month'] = df['order_date'].dt.month
    df['year'] = df['order_date'].dt.year

    print("\n--- Date Conversion Verification ---")
    print(df[['Order Date', 'order_date', 'month', 'year']].head(5))

    # --- Step 6: Data Cleaning ---
    # Final cleaning to ensure full compatibility with Tableau and other tools.

    # 1. Fill missing values in 'Postal Code'
    df['Postal Code'] = df['Postal Code'].fillna(0)

    # 2. Normalize column names (lowercase, replace spaces and hyphens with underscores)
    # This ensures names like 'sub-category' become 'sub_category'
    print("\n--- Normalizing Column Names ---")
    df.columns = [col.lower().replace(' ', '_').replace('-', '_') for col in df.columns]

    # 3. Remove duplicate columns
    # If there are two 'order_date' columns, we keep the first one and fix its type
    df = df.loc[:, ~df.columns.duplicated()]
    
    # Ensured order_date is datetime for Tableau compatibility
    # This is done after all transformations to ensure the final column is correct
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    print("Standardized naming and ensured correct data types for Tableau compatibility.")
    
    # Verify final structure and data types
    print("\n--- Final Column Names ---")
    print(df.columns.tolist())

    print("\n--- Final Data Types (Verification) ---")
    print(df.dtypes)

    # 4. Save the final cleaned dataset
    df.to_csv('data/cleaned_data.csv', index=False)
    print("\n✅ Cleaned dataset saved successfully to 'data/cleaned_data.csv'!")

except FileNotFoundError:
    print("❌ Error: 'raw_data.csv' not found. Please ensure it is in the 'data/' folder.")

# --- Step 7: Deep Analysis (Coming Soon) ---
# This is where we will calculate trends and create visualizations.
