# Practice29
my_list = [1, [1,2,3], ["hello","hi",10], 100]
my_list[2][0] = 'Python'
my_list[1].reverse()
print(my_list)

# Practice30
my_str = 'My name is Mehrdad and I love Python'
my_list = my_str.split(' ')
print(my_list)

some_list = my_list[2:5]

my_list.append('today')
my_list[-3:-2] = ['code', 'with']
my_list[-2:] = ['Python', 'everyday', '!']

print(f'some_list: {some_list}')
print(f'my_list: {my_list}')

my_str = ' '.join(my_list)
print(my_str)
