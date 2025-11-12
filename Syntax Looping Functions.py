# from _ast import arg
# from email.utils import parseaddr

name_me = "Rudolf"   # text
age = 22            # number
height = 5.4        # decimal
is_student = True   # boolean
# Print the variables
print(name_me, age, height, is_student)

#### LOOPING ####

# f-string, which allows inserting variables directly inside a string.
for i in range(5):
    print(f"Iteration {i+1}: Name is {name_me}, Age is {age}, Height is {height}, Is Student: {is_student}")

for i in range(5):
    print("Loop Number:",i)

k = 1
while k <= 3:
    print("count:",k)
    k+=0.5

#continue → skips the rest of the current iteration
#break → stops the loop early

for i in range(10):
    if i == 2:
        continue # Skips printing 2
    if i == 7:
        break  # Stops when i == 7
    print("Continue,break:",i)

#else with loops → runs when the loop finishes normally
for i in range(3):
    print(i)
else:
    print("Loop ended normally")

# nested loops
for i in range(2):
    for j in range(3):
        print("nested loop:", i, j)

#odd even
for i in range(1, 10, 2):
    print(i)  # prints odd numbers
for i in range(10, 0, -2):
    print(i)  # prints even numbers in reverse

#### FUNCTIONS ####

# Function with parameter
def greeting(name="Guest"):
    return f"Hello, {name}!"
print(greeting())         # uses default parameter
print(greeting("Rose"))   # overrides default parameter

# Function with multiple parameters
def add(a, b):
    return a+b
print(add(5,7))
print(add(10,20))
print(add(age, height))

# Function with default parameter
def multiply(x, y=2):
    return x * y
print(multiply(5))    # uses default y=2
print(multiply(5, 3)) # overrides default y=2 with y=3

# Function with variable number of arguments - returns sum
def summarize(*args):
    return sum(args)  # returns 0 for no arguments
print(summarize(1, 2, 3))         # prints 6
print(summarize(10, 20, 30, 40))  # prints 100

# Function with variable number of arguments - returns multiplication
def calculate(*args):
    product = 1
    for num in args:
        product *= num   # multiply each number
    return product

print(calculate(2, 3, 4))  # 2×3×4 = 24
print(calculate(5, 6))     # 5×6 = 30
print(calculate(age,height))

## Lambda function
print("")
print("LAMBDA FUNCTIONS")
print("")

# assign an anonymous function to a variable
sq = lambda n: n ** 2
print(sq(5))  # 25

from functools import reduce
print(reduce(lambda r, y: r / y, [100, 2, 5]))  # Output: 10

# use with map
print(list(map(lambda e: e + 1, [1, 2, 3])))

# use with filter
print(list(filter(lambda w: w % 2 == 0, range(10))))

# use as a sorting key
names = ["Alice", "bob", "Charlie"]
print(sorted(names, key=lambda s: s.lower()))

# immediate invocation
print((lambda a, b: a + b)(2, 3))

# factory that returns a lambda (closure)
def make_multiplier(factor):
    return lambda x: x * factor

double = make_multiplier(2)
print(double(7))  # 14
triple = make_multiplier(3)
print(triple(7))  # 21

import math

nums = [2, 3, 4]
result = math.prod(nums)
print(result)  # Output: 24

# lambda with default argument
t = lambda l, y=10: l + y
print(t(5))    # 15
print(t(5, 20)) # 25
print(t(height))

def intro (firstname, age_factor):
    print( f"Hello, my name is {firstname}, and I am {age_factor} years old.")
intro(age_factor=22,firstname="rudolf")


def square(m):
    return m * m
result = square(5)
print(result)  # Output: 25