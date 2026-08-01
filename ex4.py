# Format strings
color = 'red'
print('His car is ' + color) # Concatenation

print('His car is {}'.format('blue'))
print('His car is {} and his shirt is {}'.format(123, color)) # Format gets different kinds of arguments
print('Her oldest {0} is her best {0}'.format('friend'))
print('Her {1} is {0}'.format('blue', 'bag'))

print("{name}'s {object} is {color}".format(color='brown', object='headphone', name='Garshasp'))

# Format float numbers
print("My average score is {average:5.1f}".format(average=175/9))
# 10.3f: "My average score is      4.333"
#                             12345678910
