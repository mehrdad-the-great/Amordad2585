my_score = float(input('Enter your score: '))

if my_score < 10:
    print('School needs to see your parents. Sorry!')

if my_score == 20:
    my_score *= 2
    print('1st. You rock baby!')
    print('Highest score possible')
elif my_score >= 18:
    print('2nd. Very Good!')
elif my_score >= 15:
    print('3rd. Good!')
elif my_score >= 12:
    print('4th. Not bad!')
else:
    print('5th. You need to work much harder!')

print(my_score)
