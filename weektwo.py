# Create an empty list
my_list=[]
print("After creating empty list:", my_list)

# Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
print("After appending 10:", my_list)

my_list.append(20)
print("After appending 20:", my_list)

my_list.append(30)
print("After appending 30:", my_list)

my_list.append(40)
print("After appending 40:", my_list)

# Insert 15 at the second position of the list (index 1)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50,60,70]:", my_list)

# Remove the last element
my_list.pop()
print("After removing the last element:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After Sorting the list in ascending order:", my_list)

# Find and print the index of 30
index_of_30 = my_list.index(30)
print (index_of_30)
