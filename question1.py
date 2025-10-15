## Question 1:

# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Function to find the second-largest number
def second_largest(numbers):
    numbers.sort()              # Sort the list in ascending order
    return numbers[-2]          # Return the second last element

# Test the function
print("Second largest number:", second_largest(my_list))

## Answer- Second largest number: 30