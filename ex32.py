my_str = 'xyyz'
print('xyy' in my_str)

my_list = [1, 2, 'Hello', '45']
print('H' in my_list)

my_tuple = ('Hi', 'Hello', [1,2,3])
if 'Bye' in my_tuple:
    print('Bye word is in my_tuple')
else:
    print('Bye word is not in my_tuple')

my_project_runners = {'designer': 'Farzad', 'developer': 'Sanaz', 'VC': 'Mehrdad', 'HR': 'Nayeb'}
print('Sanaz' in my_project_runners.values())
print('CEO' not in my_project_runners.keys())


user = input('Enter your name to check if you are in the students list: ')
my_students = ['Mehrdad', 'ArioBarzan', 'Garshasp', 'Tahmasp', ]
if user not in my_students:
    print('Sorry {}. You\'re not in the class!'.format(user))
else:
    print('You\'re on board, baby! let\'s go :)')
print(f'Class students: {my_students}')


costumer_feedback = input('How do you feel about our product?\n')
if 'love' in costumer_feedback:
    print('Good feedback received')
elif 'hate' in costumer_feedback:
    print('Bad feedback received')
else:
    print('Neither positive nor negative feedback reveived')
