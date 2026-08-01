# Set
my_set = set()
my_set.add(4)
my_set.add(1)
my_set.add('2')
my_set.add(1)
my_set.remove(4)
print(my_set)

new_set = set([4, 5, '5', 1 , '3, 4', 1, 5])

# Delete repeated items from a list or a tuple
my_list = [1, 2, 2, 1, 3, 1, 4, 2, 1, ] # Or my_tuple = ....
print(list(set(my_list)))
