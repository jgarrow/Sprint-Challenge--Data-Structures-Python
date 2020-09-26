import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# binary search -- run time is <0.07 seconds
# assumes name_list is sorted
# def binary_search(name_list, list_len, value_to_compare):
#     lowest_index = 0 # lowest index we're looking at
#     highest_index = list_len - 1 # highest index we're looking at

#     while lowest_index <= highest_index:
#         # middle index between the current lowest_index and high
#         middle_index = int(lowest_index + ((highest_index - lowest_index) / 2))

#         # if we found a duplicate, return True
#         if name_list[middle_index] == value_to_compare:
#             return True

#         # else if the middle value too big, make highest_index 1 smaller than the middle index
#         elif name_list[middle_index] > value_to_compare:
#             highest_index = middle_index - 1
        
#         # else if the middle value is too small, make lowest_index 1 bigger than the middle index
#         else:
#             lowest_index = middle_index + 1
    
#     # return False if we never find a match
#     return False


# sorted_names_1 = sorted(names_1)


# for name_2 in names_2:
#     if binary_search(sorted_names_1, len(sorted_names_1), name_2) is True:
#         duplicates.append(name_2)
    

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# run time is <0.005 seconds
# duplicates = sorted(list(set(names_1).intersection(names_2)))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


