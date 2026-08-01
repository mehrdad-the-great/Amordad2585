def send_message_to_parents(mark):
    print(
        'Dear parents of our lovely student:\nWe need to talk with you about your son\'s mark.\n'
        'His mark is {}'.format(mark)
    )


student_mark = float(input('Enter your mark: '))
student_points = 0

if student_mark < 10:
    print('School needs to see your parents. Sorry!')
    send_message_to_parents(student_mark)
    student_points -= 10

if student_mark == 20:
    print('You rock baby!. Great job!')
    student_points += 100
elif student_mark >= 18:
    print('Very Good!')
    student_points += 85
elif student_mark >= 15:
    print('Good!')
    student_points += 70
elif student_mark >= 12:
    print('Not bad!')
    student_points += 50
else:
    print('You need to work much harder!')
    student_points += 20

print(f'You have {student_points} points.')
