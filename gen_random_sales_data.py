import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start, end):
    """Generate a random date between `start` and `end`."""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Define the start and end dates
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# List of products
products = ["Soccer Ball", "Tennis Racket", "Basketball", "Baseball Glove", "Skateboard", "Running Shoes"]

# Price range for each product (min and max)
prices = {
    "Soccer Ball": (15, 30),
    "Tennis Racket": (50, 200),
    "Basketball": (20, 40),
    "Baseball Glove": (25, 100),
    "Skateboard": (30, 120),
    "Running Shoes": (60, 150)
}

# Generate the data
data = []
for _ in range(1000):
    product = random.choice(products)
    price_range = prices[product]
    price = round(random.uniform(*price_range), 2)
    quantity = random.randint(1, 10)
    date = random_date(start_date, end_date).strftime("%Y-%m-%d")

    data.append([date, product, price, quantity])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Date", "Product", "Price", "Quantity"])

# Save to CSV
csv_file_path = 'sales_data.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path
