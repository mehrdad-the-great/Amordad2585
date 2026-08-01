# Practice37
user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
user_nation = input('Where are you from? ')

print(f'Hello {user_name}. You are {user_age} years old and you\'re from {user_nation}. Thank you! :)')
print("Hello {}. You are {} years old and you're from {}. Thank you! :)".format(user_name, user_age, user_nation))


# Practice38
person_details = {
"name": "Ana",
"age": 28,
"languages": ["Python", "Java", "C"]
}
# Name
print(person_details['name'])
# Languages
print(person_details['languages'])
# Change the third item of the 'languages' list to 'C++'
person_details['languages'][-1] = 'C++'
print(person_details["languages"])
