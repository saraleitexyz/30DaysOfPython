# Day 1 - 30DaysOfPython Challenge

"""
Exercise: Level 2

Create a folder named day*1 inside 30DaysOfPython folder. 
Inside day_1 folder, create a python file helloworld.py and 
repeat questions 1, 2, 3 and 4. Remember to use \_print()* when 
you are working on a python file. Navigate to the directory where 
you have saved your file, and run it.
"""


# 1. Check the python version you are using:
import sys
print(sys.version)

"""
2. Open the python interactive shell and do the following operations. 
The operands are 3 and 4.
"""
print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 % 4)             # modulus(%)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 // 4)            # Floor division operator(//)

"""
3. Write strings on the python interactive shell. 
The strings are the following:
"""
print('Sara')
print('Leite')
print('Spain')
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data:
print(type(10))        
print(type(9.8))   
print(type(3.14))        
print(type(4 - 4j))        
print(type(['Asabeneh', 'Python', 'Finland']))  
print(type('Sara'))   
print(type('Leite'))   
print(type('Spain'))

"""
Exercise: Level 3

1. Write an example for different Python data types such 
as Number(Integer, Float, Complex), String, Boolean, List, Tuple, 
Set and Dictionary.
"""
print(6)                    # Number (integer)
print(6.3)                  # Number (float)
print(3j)                   # Number (Complex)
print('hey')                # String
print(True)                 # Boolean
print([0, 1, 2])              # List
print(('Mars', 'Venus'))    # Tuple
print({2, 4, 3, 5})         # Set
print({
'first_name':'Sara',
'last_name':'Leite',
'country':'Spain'
})                          # Dictionary

# 2. Find an Euclidian distance between (2, 3) and (10, 8).
import math

point1 = (2, 3)
point2 = (10, 8)

distance = math.dist(point1, point2)

print(distance)
