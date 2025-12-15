import pandas as pd
import numpy as np
from datetime import datetime

# Generate sample data
num_records = 1000

data = {
    'Customer_key': range(1, num_records + 1),
    'Name': [f'Customer_{i}' for i in range(1, num_records + 1)],
    'Address': [f'{np.random.randint(100, 9999)} Main Street, City-{i}' for i in range(1, num_records + 1)],
    'Country_key': np.random.randint(1, 50, num_records),
    'Phone': [f'+{np.random.randint(1, 99)}-{np.random.randint(100, 999)}-{np.random.randint(1000, 9999)}' for _ in range(num_records)],
    'Account_balance': np.random.uniform(1000, 100000, num_records).round(2),
    'MKS_Segment': np.random.choice(['RETAIL', 'CORPORATE', 'ENTERPRISE'], num_records),
    'Comment': [f'Sample comment for customer {i}' for i in range(1, num_records + 1)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as parquet file
output_file = 'customer_data.parquet'
df.to_parquet(output_file, index=False)

# Verify the file was created
print(f"Parquet file '{output_file}' has been created successfully")
print(f"Number of records: {len(df)}")
print("\nFirst 5 records:")
print(df.head())