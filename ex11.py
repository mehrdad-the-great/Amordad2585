# Review4
# List
my_list = [2, 50, 'Hello', -1, 1.5]

a = '3'
b = {'x': 'length', 'y': 'width', }
c = 5
d = 4.5
e = ('x', 'y')
f = [1, 2, 3]

my_list.append(a)
# [2,..., '3']
my_list.insert(2, c)
# [2, 50, 5, 'hello', -1, 1.5, '3']

# my_list.extend([b, d, e, ]) or below one
my_list += [b, d, e, ]
# [2,..., '3', b, d, e, ]

my_list[4] = f
# [2, 50, 5, 'hello', f, 1.5, '3', b, d, e]

# Remove item and return it
popped_item = my_list.pop(2)
print(f'{popped_item} popped out')
# [2, 50, 'hello', f, 1.5, '3', b, d, e]

# Remove item without returning it : remove() removes the first item which is equal to it's given argument
my_list.remove('3')
# [2, 50, 'hello', f, 1.5, b, d, e]

my_list[:3] = ['Slicing']
# ['slicing', f, 1.5, b, d, e]
print(my_list)


my_list = [3, 3.5, -4, 1, 0, 1]
my_list.sort()
my_list.reverse()
print(min(my_list), max(my_list))
print(my_list)
