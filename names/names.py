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



# assumes name_list is sorted
def binary_search(name_list, list_len, value_to_compare):
    low = 0 # lowest index we're looking at
    high = list_len - 1 # highest index we're looking at

    while low <= high:
        # print('\nlow: ', low)
        # print('high: ', high)
        # middle index between the current low and high
        mid = int(low + ((high - low) / 2))
        # print('mid: ', mid)

        # if we found a duplicate, return True
        if name_list[mid] == value_to_compare:
            return True

        # else if the middle value too big, make high 1 smaller than the middle index
        elif name_list[mid] > value_to_compare:
            high = mid - 1
        
        # else if the middle value is too small, make low 1 bigger than the middle index
        else:
            low = mid + 1
    
    # return False if we never find a match
    return False


sorted_names_1 = sorted(names_1)


for name_2 in names_2:
    if binary_search(sorted_names_1, len(sorted_names_1), name_2) is True:
        duplicates.append(name_2)
    

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
