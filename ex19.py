# Practice 25
my_list = [18, 19, 102, -4, 0, ]
# Add number 54 to the end
my_list.insert(5, 54)
my_list.append(54)
my_list += [54]
my_list.extend([54])

print(len(my_list))
print(my_list[0], my_list[2], my_list[-5::2])
print(my_list[:4] + my_list[4:])    # -> my_list

print(my_list[1:4])
my_list[1:4] = [1]
print(my_list)


# Practice26-27
# ۵ ،۹ ،۱۴ ،۱۲ ،۱۰ ،۱ ، -۴ -و ۹ 
my_list = [5, 9, 14, 12, 10, -1, -4, 9]
print(len(my_list), my_list[7])

my_list = ['Hello', 1, [], {'1st': 'Hi', '2nd': 'Hello', '3rd': 'Hey'}, 2, -1.5, 0, ('Hello', 'Hi', 'Hey',),]
poped_item = my_list.pop(3)
print(poped_item['2nd'])

# Practice28
my_numbers = [5, 2, 8, -1, 2, 9, 0]

my_numbers_sorted = my_numbers.copy()
my_numbers_sorted.sort()
print(my_numbers, my_numbers_sorted)
