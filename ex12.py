# Review6
# Calculate environment and area of a circle
radius = float(input('Enter the radius of the circle: '))
pi = 3.14

environment = 2 * pi * radius
area = pi * (radius ** 2)

# print('Environment: {:5.2f} , Area: {:5.2f}'.format(environment, area)) or below one
print('Environment: {environment:5.2f} , Area: {area:5.2f}'.format(environment=environment, area=area))
