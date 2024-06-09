#1. Provide an example where changing a mutable object inside a function affects the original object outside the function.
def callby_reference(a):
    print(f"before changing value of 'a' is --- {a}")

    a = 90
    print(f"after changing value of 'a' is --- {a}")
    return a


a = 5
print(f"after function call the value of 'a' is --- {callby_reference(a)}")
#----------------------------------------------------------------------------------------

#2. What is PyLint, and how is it used in Python code auditing? Explain with  a sample example.

"""
This module is for audio calling feature
"""


def mute_audio():
    """
    This function is for audio mute
    :return:
    """
    print("Mute audio")


mute_audio()


def unmute_audio():
    """
    This function is for audio unmute
    :return:
    """
    print("Unmute audio")


unmute_audio()

"""
o/p --- 
[notice] A new release of pip is available: 23.2.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip


------------------------------------
Your code has been rated at 10.00/10

"""


#-----------------------------------------------------------------------------


#3. Write a program using a for loop and list comprehensions to find all prime numbers in a given range.

#using for loop
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_for_loop(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Example usage
start_range = 10
end_range = 50
prime_numbers = find_primes_for_loop(start_range, end_range)
print("Prime numbers using for loop:", prime_numbers)

"""
o/p--
Prime numbers using for loop: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

"""


#using list comprehension

def is_prime(num):
    if num <= 1:
        return False
    return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def find_primes_list_comprehension(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]


# Example usage
start_range = 10
end_range = 50
prime_numbers = find_primes_list_comprehension(start_range, end_range)
print("Prime numbers using list comprehension:", prime_numbers)
"""
o/p--
Prime numbers using list comprehension: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""


#--------------------------------------------------------------------------------------------------------------------

#4. Explain the concept of short-circuit evaluation in if-else blocks with examples.
#AND
def short_circuit():
    print("short circuit operation")
    return True


if False and short_circuit():
    print("This will not be printed")
else:
    print("Short-circuit evaluation with AND")


# Output:
# Short-circuit evaluation with AND


#OR

def short_circuit():
    print("short circuit operation")
    return True


if True or short_circuit():
    print("Short-circuit evaluation with OR")
else:
    print("This will not be printed")

# Output:
# Short-circuit evaluation with OR
#--------------------------------------------------------------------------------------------------------------------
"""
#5. Write a Python program using a while loop to implement a simple text-based menu system.
def show_menu():
    print("\nMenu:")
    print("1. Greet")
    print("2. Add two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")


def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")


def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product is: {result}")


def main():
    while True:
        show_menu()
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            greet()
        elif choice == '2':
            add_numbers()
        elif choice == '3':
            multiply_numbers()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

"""
#--------------------------------------------------------------------------------------------------------------------
#6. How can you use range() to iterate over indices of a list?

my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2

print(my_list)


#--------------------------------------------------------------------------------------------------------------------
#7. Explain how Python's handling of mutable and immutable types in function calls can lead to unexpected behavior. Provide an example. With Call by value and call by reference concept.
# mutable type
def callby_reference(list):
    print(f"Original list: {list}")
    list.append(5)
    print(f"Modified New list inside function: {list}")
    return list


original_list = [1, 2, 3, 4]
print(f"After function call list is {callby_reference(original_list)}")
print(f"items of list after finishing function call is -- {original_list}")
"""
o/p---
Original list: [1, 2, 3, 4]
Modified New list inside function: [1, 2, 3, 4, 5]
After function call list is [1, 2, 3, 4, 5]


"""


#immutable type
def callby_reference(a):
    print(f"Original value of 'a' is : {a}")
    a += 10
    print(f"Modified value of 'a' inside function is : {a}")
    return a


a = 5
print(f"After function call value of 'a' is {callby_reference(a)}")
print(f"value of 'a' after finishing function call is -- {a}")
"""
o/p---
Original value of 'a' is : 5
Modified value of 'a' inside function is : 15
After function call value of 'a' is 15
value of 'a' after finishing function call is -- 5

"""
#--------------------------------------------------------------------------------------------------------------------
#8. Discuss the use of lambda functions in Python with examples.

lambda_fun = lambda x, y: x + y
print(f"Addition of x+y using lambda is : {lambda_fun(5, 5)}")
"""
o/p--
Addition of x+y using lambda is : 10
"""

map_fun = lambda item: item ** 2
my_list = [1, 2, 3, 4, 5]
result = map(map_fun, my_list)
print(f"Mapping of (item ** 2) to list using map function is : {list(result)}")
"""
o/p---
Mapping of (item ** 2) to list using map function is : [1, 4, 9, 16, 25] 
"""
filter_fun = lambda item: item % 2 == 0
my_list = [1, 2, 3, 4, 5]
result = filter(filter_fun, my_list)
print(f"Filtering of (item % 2) to list using filter function is : {list(result)}")

"""
o/p--
Filtering of (item % 2) to list using filter function is : [2, 4]
"""
from functools import reduce

anonymous_fun = lambda x, y: x + y
range_list = range(2, 7)
result = reduce(anonymous_fun, range_list)
print(f"Reduce of (x+y)  items to range list of (2,7) using reduce function is : {(result)}")
from functools import reduce

"""
o/p--
Reduce of (x+y)  items to range list of (2,7) using reduce function is : 20
"""
#--------------------------------------------------------------------------------------------------------------------
#9 How do you handle exceptions in Python? Provide an example using try-except blocks.

try:
    list = [1, 2, 3, 4, 5]
    if list:
        list.append(6)
        print(f"this is list -- {list}")
    else:
        print("This is not a list")
except Exception as err:
    print(f"Error: {err}")
"""
o/p---
this is list -- [1, 2, 3, 4, 5, 6]
"""
#--------------------------------------------------------------------------------------------------------------------
#10. What are list comprehensions and dictionary comprehensions? Provide examples.

#list comprehension
squares_list = [x ** 2 for x in range(1, 10)]
print(f"squaring of items using list comprehension -- {squares_list}")
"""
o/p--
squaring of items using list comprehension -- [1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

#dict comprehension
squares_dict = {x: x ** 2 for x in range(1, 10)}
print(f"squaring of items using dict comprehension -- {squares_dict}")
"""
o/p--
squaring of items using dict comprehension -- {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
"""


#--------------------------------------------------------------------------------------------------------------------

#12. What are decorators in Python? Write a simple decorator function.
def join_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.join("555555")  #withoutspace

    return wrapper


@join_decorator
def string(name):
    return " --This method is used to join the given letter in between these words-- "


print(string(5))

"""
o/p---
5 --This method is used to join the given letter in between these words-- 5 --This method is used to join the given letter in between these words-- 5 --This method is used to join the given letter in between these words-- 5 --This method is used to join the given letter in between these words-- 5 --This method is used to join the given letter in between these words-- 5

"""
#--------------------------------------------------------------------------------------------------------------------

#13. Explain the LEGB rule in Python scope. Provide examples for Local, Enclosed, Global, and Built-in scopes.
global_var = " I am global variable"


def enclosed_function():
    enclosed_var = "I am enclosed variable"

    def local_function():
        local_var = "I am local variable"
        print(f"local function accessing variables:")
        print(enclosed_var)
        print(local_var)
        print(global_var)

    local_function()


enclosed_function()
print(f" Accessing global variable outside function - {global_var}")
"""
o/p---
local function accessing variables:
I am enclosed variable
I am local variable
 I am global variable
 Accessing global variable outside function -  I am global variable
"""


#--------------------------------------------------------------------------------------------------------------------

#14. What are private, protected, and global variables in Python? Provide examples of each.

# private variable
class Private:
    def __init__(self):
        self.__private_var = "I am private variable"

    def get_private_var(self):
        return self.__private_var


obj = Private()
print(obj.get_private_var)
"""
o/p---
<bound method Private.get_private_var of <__main__.Private object at 0x0000011FC3E75490>>
"""


# protected variable
class Protected:
    def __init__(self):
        self._protected_var = "I am protected variable"

    def get_protected_var(self):
        return self._protected_var


obj = Protected()
print(obj.get_protected_var)
"""
o/p---
<bound method Protected.get_protected_var of <__main__.Protected object at 0x0000011FC3E74050>
"""
# global variable
global_var = "I am global variable"


def get_global_var():
    print(f"global var inside fun -- {global_var}")
    return global_var


print(f"global var outside fun -- {get_global_var()}")

"""
o/p--
global var inside fun -- I am global variable
global var outside fun -- I am global variable
"""


#--------------------------------------------------------------------------------------------------------------------
#15. What is slicing ? Write a sample program to reverse a string.

def reverse_string(input_string):
    return input_string[::-1]


input_str = "This is slicing concept"
reversed_str = reverse_string(input_str)
print("Original string:", input_str)
print("Reversed string:", reversed_str)
"""
o/p---
Original string: This is slicing concept
Reversed string: tpecnoc gnicils si sihT
"""