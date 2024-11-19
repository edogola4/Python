# Create an empty list called my_list.
''' my_list = [] initializes an empty list.'''

my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
'''=> my_list.append(10), my_list.append(20), my_list.append(30), my_list.append(40) appends the given elements to the end of the list.
=> append() adds elements one by one to the list.
'''

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# # Step 3: Insert the value 15 at the second position (index 1)
'''=> my_list.insert(1, 15) inserts the value 15 at the index 1 (second position) of the list.
=> insert() adds an element at a specific index in the list.
'''

my_list.insert(1, 15)

# # Step 4: Extend my_list with another list: [50, 60, 70]
'''=> my_list.extend([50, 60, 70]) extends the list by adding all elements of the given list to the end of the original list.
=> extend() adds multiple elements to the end of the list.
'''

my_list.extend([50, 60, 70])

# # Step 5: Remove the last element from my_list

my_list.pop()

# # Step 6: Sort my_list in ascending order

my_list.sort()

# # Step 7: Find and print the index of the value 30

index_of_30 = my_list.index(30)


# # Display the results

print("Final List:", my_list)
print("Index of 30:", index_of_30)
