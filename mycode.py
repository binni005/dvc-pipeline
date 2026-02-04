import pandas as pd
import os

# Create a sample dataframe
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 65000, 70000]
})

# Create data folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save to CSV
df.to_csv('data/mydata.csv', index=False)

print("Data saved to data/mydata.csv")