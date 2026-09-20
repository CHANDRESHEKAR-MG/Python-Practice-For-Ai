revenue=50
expenses=10
print(type(revenue) ) #python is a dynamically typed language, 
                    #so the type of the variable is determined at runtime. In this case, the type of the variable 'revenue' is <class 'int'> since it is assigned an integer value of 50.
profit=revenue-expenses
print(profit) #This will output the value of profit, which is 30 in this
margin=profit*100/revenue
print(margin) #This will output the value of margin, which is 0.6

# String data type
description = "This is a string variable" # double quotes can be used to define a string variable in Python.
print(description) #This will output the type of the variable 'description', which is <class 'str'>
description = description + 'that can hold text data.' # single quotes can also be used to define a string variable in Python. 
                                   #In this case, we are concatenating the string variable 'description' with another string using the '+' operator.
print(type(description)) #This will output the type of the variable 'description', which is <class 'str'>
print(description) #This will output the value of the variable 'description', which is a string.
# Multiple Line String
description = """ This is a multiple line string variable
i llove python programming language
i love python programming language
"""

print(description) #This will output the value of the variable 'description', which is a multiple line string.

print(len(description)) #This will output the length of the variable 'description', which is 90 in this case.




