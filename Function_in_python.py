# Function in Python is a block of code that performs a specific task and can be reused multiple times in a program.
# Functions are defined using the def keyword followed by the function name and parentheses.


def calculate_margin(revenue: float, expenses: float) -> tuple[float, float]:
    
    profit = revenue - expenses
    margin = (profit / revenue) * 100 if revenue != 0 else 0.0
    
    return profit, margin


revenue = 50
expenses = 30

profit, margin = calculate_margin(revenue, expenses)
print(f"Profit: {profit}") # here f is used bcz 
print(f"Margin: {margin}%")

response = calculate_margin(revenue, expenses)
print(response[0])
print(response[1])


def total_expenses(exp1,exp2):
    return exp1+exp2
print(total_expenses(2, 3))

def calc_total_expenses(*args):# to add multiple numbers with a single parameter with *args
    
    return sum(args)


print(calc_total_expenses(2, 3, 5, 2, 8))  # pass the dynamic number parameter 


def  expenses(rent, phone_bill):
    return rent+phone_bill

print(expenses(rent=1000,phone_bill=30))


def calc_total_Billexpenses(**kargs):
    # sum the values passed as keyword arguments
    # return (kargs.values())
    print(kargs)

calc_total_Billexpenses(rent=100, phone_bill=30)

def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers))


# ** can unpack a dictionary:

def student(name, age):
    print(name, age)

data = {
    "name": "Chandu",
    "age": 21
}

student(**data)



def add(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20, 30))
print(add(5, 10, 15, 20, 25))

def add(*numbers):
    print(numbers)

add(10, 20, 30)

#**kwargs — Multiple keyword arguments

#**kwargs collects multiple keyword arguments into a dictionary.

#Example:

def student(**kwargs):
    print(kwargs)

student(name="Chandu", age=21, branch="CSE")


#You can access values using keys:

def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["branch"])

student(name="Chandu", branch="CSE")

#You can also loop:

def student(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

student(name="Chandu", age=21, branch="CSE")

# Using both together

# You can use both in the same function:

def student(*args, **kwargs):
    print(args)
    print(kwargs)

student("CSE", 21, name="Chandu", city="Mandya")



# Main difference
# 	*args	**kwargs
# Accepts	Positional arguments	Keyword arguments
# Stores as	Tuple	Dictionary
# Example	10, 20, 30	name="Chandu", age=21
# Meaning	Any number of values	Any number of named values


# 1. Student marks calculator — *args

# Suppose you don't know how many subjects a student has:

def calculate_marks(*marks):
    total = sum(marks)
    average = total / len(marks)

    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)


calculate_marks(85, 76, 91, 88, 79)


#Shopping cart — *args
def shopping_cart(*items):
    print("Your cart:")

    for item in items:
        print("🛒", item)


shopping_cart("Laptop", "Mouse", "Keyboard", "Headphones")


# 3. Student profile — **kwargs

# This is a very realistic use of **kwargs:

def create_profile(**details):
    print("Student Profile")

    for key, value in details.items():
        print(key, ":", value)


create_profile(
    name="Chandu",
    branch="CSE",
    year=4,
    skills=["Java", "Python", "SQL"]
)