# Comparison: < > <= >= == != and or
# comparison between int and str is only allowed with != ==
print('5' + '0' * 4 == 5 * 10 ** 4)
# '50000' != 50000

user_age = 25
user_name = 'Mehrdad Faokhzad'
print(18 <= user_age <= 45 or len(user_name) < 9)

user_mark = 18.5
class_avg_mark = 15
minimum_passing_mark = 12
print(user_mark > class_avg_mark and user_mark > minimum_passing_mark)

a = 300
print(a > 100 and a <= 200)
print(a != 300 or a > 0)
print(('Hello' == 'Hi') and (a != 0))

print(a > 100 or a < 200)   # Always True
print(a < 200 and a > 250)  # Always False

account_deposit = 1250
account_credit = 2500
debt = 1500
print('Can he pay his debt?')
if debt <= account_deposit or debt <= account_credit:
    print('Yes.')
    if debt <= account_deposit:     # Our first priority to pay is our deposit
        print('He will pay from his deposit.')
    else:
        print('He will pay from his credit.')
else:
    print('No.')
