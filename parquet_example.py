import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime, timedelta
import numpy as np

# Generate sample e-commerce transaction data
np.random.seed(42)
n_records = 100000

# Create realistic e-commerce data
data = {
    'transaction_id': [f'TXN_{i:06d}' for i in range(n_records)],
    'customer_id': np.random.randint(1000, 50000, n_records),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_records),
    'product_id': [f'PROD_{i:05d}' for i in np.random.randint(1, 10000, n_records)],
    'quantity': np.random.randint(1, 10, n_records),
    'unit_price': np.round(np.random.exponential(50) + 10, 2),  # Price distribution
    'discount_percent': np.random.choice([0, 5, 10, 15, 20], n_records, p=[0.4, 0.2, 0.2, 0.15, 0.05]),
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'], n_records),
    'transaction_date': [
        datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) 
        for _ in range(n_records)
    ],
    'customer_age': np.random.randint(18, 80, n_records),
    'customer_state': np.random.choice(['CA', 'NY', 'TX', 'FL', 'WA'], n_records)
}

# Calculate total amount
df = pd.DataFrame(data)
df['total_amount'] = df['quantity'] * df['unit_price'] * (1 - df['discount_percent'] / 100)

print("Sample of the dataset:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Write to Parquet with partitioning by date (year-month)
df['year_month'] = df['transaction_date'].dt.strftime('%Y-%m')

# Save as regular CSV for comparison
df.to_csv('ecommerce_data.csv', index=False)

# Save as Parquet file
df.to_parquet('ecommerce_data.parquet', index=False, compression='snappy')

# Save as partitioned Parquet (realistic lakehouse structure)
df.to_parquet(
    'ecommerce_partitioned.parquet',
    partition_cols=['year_month', 'product_category'],
    compression='snappy',
    index=False
)

# Read back and demonstrate performance benefits
print("\n" + "="*50)
print("FILE SIZE COMPARISON:")
print("="*50)

import os
csv_size = os.path.getsize('ecommerce_data.csv') / 1024**2
parquet_size = os.path.getsize('ecommerce_data.parquet') / 1024**2

print(f"CSV file size: {csv_size:.2f} MB")
print(f"Parquet file size: {parquet_size:.2f} MB")
print(f"Compression ratio: {csv_size/parquet_size:.1f}x smaller")

# Demonstrate column pruning (only read specific columns)
print("\n" + "="*50)
print("COLUMN PRUNING EXAMPLE:")
print("="*50)

# Read only specific columns
selected_columns = ['customer_id', 'total_amount', 'transaction_date']
df_subset = pd.read_parquet('ecommerce_data.parquet', columns=selected_columns)
print(f"Read only {len(selected_columns)} columns out of {len(df.columns)}")
print(df_subset.head())

# Demonstrate predicate pushdown (filtering during read)
print("\n" + "="*50)
print("PREDICATE PUSHDOWN EXAMPLE:")
print("="*50)

# Filter for high-value transactions while reading
high_value_transactions = pd.read_parquet(
    'ecommerce_data.parquet',
    filters=[('total_amount', '>', 200)]
)
print(f"Filtered {len(high_value_transactions)} high-value transactions out of {len(df)}")
print(high_value_transactions[['customer_id', 'total_amount', 'product_category']].head())

# Show basic file info instead of detailed schema
print("\n" + "="*50)
print("PARQUET FILE INFO:")
print("="*50)

# Read parquet file info
try:
    df_info = pd.read_parquet('ecommerce_data.parquet')
    print(f"Parquet file contains {len(df_info)} rows and {len(df_info.columns)} columns")
    print("Column types:")
    print(df_info.dtypes)
except ImportError:
    print("Note: Install pyarrow for advanced Parquet features like schema inspection")
    print("Run: pip install pyarrow")

# Real-world use case example
print("\n" + "="*60)
print("REAL-WORLD USE CASE: MONTHLY SALES ANALYTICS")
print("="*60)

# Simulate a common analytics query
monthly_sales = (df.groupby(['year_month', 'product_category'])
                 .agg({
                     'total_amount': ['sum', 'mean', 'count'],
                     'customer_id': 'nunique'
                 })
                 .round(2))

monthly_sales.columns = ['total_revenue', 'avg_order_value', 'order_count', 'unique_customers']
print("Monthly sales by category:")
print(monthly_sales.head(10))

print("\n" + "="*50)
print("WHY PARQUET IS PERFECT FOR THIS USE CASE:")
print("="*50)
print("""
1. COLUMNAR STORAGE: Only reads 'total_amount' and 'customer_id' columns for aggregation
2. COMPRESSION: 3x smaller than CSV, faster I/O
3. PREDICATE PUSHDOWN: Can filter by date range without reading full dataset  
4. SCHEMA EVOLUTION: Can add new columns without breaking existing queries
5. METADATA: Built-in statistics enable query optimization
6. PARTITIONING: Data organized by year_month for efficient time-based queries
""")

"""
# Clean up files (optional)
import shutil
try:
    os.remove('ecommerce_data.csv')
    os.remove('ecommerce_data.parquet')
    shutil.rmtree('ecommerce_partitioned.parquet')
    print("\nCleanup completed - demo files removed")
except:
    print("\nNote: Some demo files may remain for your exploration")
"""