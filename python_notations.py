# Slicing a list
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  # Extracts elements from index 1 to 3 (not including 4)
print(sliced_list)  # Output: [2, 3, 4]

# Reversing a string
my_string = "Hello, World!"
reversed_string = my_string[::-1]  # Reverses the string
print(reversed_string)  # Output: "!dlroW ,olleH"

# Creating a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating a dictionary with squares of numbers from 1 to 5
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Defining a lambda function to calculate the square of a number
square = lambda x: x**2
print(square(5))  # Output: 25


# Defining a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# Applying the decorator to a function
@my_decorator
def say_hello():
    print("Hello!")


say_hello()  # Output: "Something is happening before the function is called."
#          "Hello!"
#          "Something is happening after the function is called."

# Using f-strings for string formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Output: "Alice is 30 years old."


data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)

set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")
