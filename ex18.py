# Practice23
a = 2
b = 3
print(a ** (b + 1))     # 2 ** 4 = 16

name = "Mehrdad"
family_name = "Farokhzad"
print(name, family_name)
job = "Developer"

print(f'I am {name} {family_name}. I am a {job}.')
print('I am {} {}. I am a {}'.format(name, family_name, job))


# Practice24
greeting_message = 'Hello everybody!'
name = 'Mehrdad'
age = 27
favorite_language = 'Python'

print(
    '{greet} My name is {name}. I am {age} years old and I absolutely love {language} programming language'
    .format(
        greet=greeting_message, name=name, age=age, language=favorite_language,
    )
)
print(
    f'{greeting_message} My name is {name}. '
    f'I am {age} years old and I absolutely love {favorite_language} programming language'
)
