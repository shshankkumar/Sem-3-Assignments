import numpy as np
import pandas as pd

# Create NumPy array of product prices
prices = np.array([50, 120, 80, 200, 150])

# Calculate mean, median, maximum and minimum price
mean_price = np.mean(prices)
median_price = np.median(prices)
maximum_price = np.max(prices)
minimum_price = np.min(prices)

print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Maximum Price:", maximum_price)
print("Minimum Price:", minimum_price)

# Create Pandas DataFrame
data = {
    "Product": ["Rice", "Milk", "Sugar", "Oil", "Biscuits"],
    "Price": prices,
    "Quantity": [15, 8, 20, 5, 12]
}

df = pd.DataFrame(data)

print("\nGrocery Inventory:")
print(df)

# Display items having quantity less than 10
print("\nItems having quantity less than 10:")
print(df[df["Quantity"] < 10])

#OUTPUT:
#Mean Price: 120.0
#Median Price: 120.0
#Maximum Price: 200
#Minimum Price: 50

#Grocery Inventory:
#    Product  Price  Quantity
#0      Rice     50        15
#1      Milk    120         8
#2     Sugar     80        20
#3       Oil    200         5
#4  Biscuits    150        12

#Items having quantity less than 10:
#  Product  Price  Quantity
#1    Milk    120         8
#3     Oil    200         5