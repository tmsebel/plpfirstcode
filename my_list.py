# This is an empty list called my_list.
my_list = []

# Append the  elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print the index of 30
print(my_list.index(30))

# Optional: Print the final list to see all values
print(my_list)