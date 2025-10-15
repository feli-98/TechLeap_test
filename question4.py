## Question 4:

# Write a short function to calculate the total revenue.

def calculate_total_sales(data):
    return sum(item["price"] * item["quantity"] for item in data)

# Sample dataset
sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

# Calculate and print total revenue
total = calculate_total_sales(sales_data)
print("Total revenue:", total)

## Answer- Total revenue: 1260