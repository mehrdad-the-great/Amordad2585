# Practice1
print(23 + 45 + -7)
print(23 + 45 - 7)

# Practice2
result1 = 23 + 45 + (-7)
print(result1)

# Practice3,4
print(3 + 4 * 5 + (-7 -- (-4)) ** 2 - 13 // 2 + 15 % 6 / 2.5) # first % then /

a = 5 -- -2
b = -1
c = 30
d = c // 2
c = 1   # Does not affect on the rest of the code
e = d % 12
f = -4 ** 2
result = a + b - e - 3 * f
# result = 5 --- 2 + (-1) - (30 // 2) % 12 - 3 * (-4 ** 2)
# 5 - 2 -1 - 15 % 12 - 3 * -16 = 2 - 3 + 48 = 47
print(result)


a = 4 * 5
b = -7 -- -4
c = pow(b, 2)
d = 13 // 2
e = 15 % 6
f = e / 2.5
result = 3 + a + c - d + f

print(result)

# Practice5,6
print(((2 ** 10) * (15 + -3)) + (3 * 1000))

# Practice7
x = 3.14 * 3
y = x ** 3
print(y)

# Practice 8-11
print((12 / 6))
# float + float -> float        int + float -> float
# float * float -> float        int * float -> float
# float // float -> float       int // float -> float
# float % float -> float       int % float -> float
print(type(1 + 2.5 - 3))
print(type(1.5 + 2.5))
print(type(1.5 * 2))
print(type(4 // 2.5))
print(3 % 2)
