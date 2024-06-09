"""

DECORATORS -- These are callable objects that take a function and return the modified function without changing the original function
"""


def process_text(text):
    text = text.strip()  # Remove leading and trailing whitespace
    text = text.capitalize()  # Capitalize the first letter
    words = text.split()  # Split into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    result = " ".join(reversed_words)  # Join words back into a single string
    return result


input_text = "   komal   "
output_text = process_text(input_text)
print(output_text)


# Output: lamok


#ADDING DECORATOR
def adding_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@adding_decorator
def add(a, b):
    return a + b


print(f"result is --- {add(5, 10)}")

"""
o/p ---
Calling add with args: (5, 10), kwargs: {}
add returned: 15
result is --- 15

"""


# MULTIPLICATION DECORATOR

def multiplying_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@multiplying_decorator
def mul(a, b):
    return a * b


print(f"result is --- {mul(5, 10)}")

"""
o/p ---
Calling mul with args: (5, 10), kwargs: {}
mul returned: 50
result is --- 50

"""


# SUBTRACTION DECORATOR

def subtrating_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@subtrating_decorator
def sub(a, b):
    return a - b


print(f"result is --- {sub(5, 10)}")

"""
o/p ---
Calling sub with args: (5, 10), kwargs: {}
sub returned: -5
result is --- -5

"""


# SUBTRACTION DECORATOR

def division_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@division_decorator
def div(a, b):
    return a / b


print(f"result is --- {div(5, 10)}")

"""
o/p ---
Calling div with args: (5, 10), kwargs: {}
div returned: 0.5
result is --- 0.5

"""

"""
def f1():
    start = time.time()
    print(f"function {f1.__name__} execution started")
    for item in range(10):
        print("India")
        print("Python")
    end = time.time()
    print(f"function {f1.__name__}execution took {end - start} seconds")


print("\n")


def f2():
    start = time.time()
    print(f"function {f1.__name__} execution started")
    for item in range(100):
        print(f"Current item is {item}")
    end = time.time()
    print(f"function {f2.__name__} execution took {end - start} seconds")


print("\n")


def f3():
    start = time.time()
    print(f"function {f3.__name__} execution started")
    for item in range(500):
        pass
    end = time.time()
    print(f"function {f3.__name__} execution took {end - start} seconds")


f1()
f2()
f3()
print("\n")
import time


def get_fun_running_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"function {fun.__name__} execution started")
        fun()  # Original function execution
        end = time.time()
        print(f"function {fun.__name__} execution took {end - start} seconds")

    return wrapper


@get_fun_running_time
def f1():
    for item in range(10):
        print("India")
        print("Python")


print("\n")


@get_fun_running_time
def f2():
    for item in range(10):  # range(10) -> [0,1....9]
        print("India")
        print("Python")


@get_fun_running_time
def f3():
    time.sleep(5)


# f1()
# f2()
f3()
print("\n")


def make_up(fun):
    print("Make up Started")

    def wrapper(*args, **kwargs):
        print(f"Person arrived..")
        result = fun()  # Original fun triggered
        print(f"Make has been completed for {result} .. Next person please...")

    return wrapper


@make_up
def person_name():
    return "John Doe"


person_name()
print("\n")


# Database info after sign up
facebook = {"email": "john@gmail.com", "password": "Welcome@123"}


def login(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} being executed....")

        result = func()  # Original
        # Logic to check valid user or not
        if facebook["email"] == result["email"] and facebook["password"] == result["password"]:
            return True  # Valid user
        else:
            return False  # InValid user

    return wrapper


@login
def user1():
    return {"email": "johndoe@gmail.com", "password": "Welcome@123"}


res = user1()
if res == True:
    print("User is successfully authenticated with valid credentials")
else:
    print("Invalid EMail/Password.. Try again!")


# Write a decorator to split a string
def split_str(fun):
    def wrapper(*args, **kwars):
        original_str = fun()
        res = original_str.split(",")
        return " ".join(res)

    return wrapper


@split_str
def get_str():
    return "Hello,Everyone,Welcome,to,Python"


print(get_str())
#eg1 insta login decorator

insta = {"email": "komal123@gmail.com", "password": "komal@05"}


def login_decorator(func):
    print(f"Entered function is: {func.__name__}")

    def wrapper(*args, **kwargs):
        result = func()
        if insta["email"] == result["email"] and insta["password"] == result["password"]:
            return insta["email"]
        else:
            return False

    return wrapper


@login_decorator
def user1_login():
    return {"email": "komal123@gmail.com", "password": "komal@05"}


res = user1_login()
if res:
    print(f"Login Successful for user {user1_login()}")
else:
    print(f"{user1_login()} is Not a certified user - Login Failed  ")


#eg2 printing name 5 times
def repeat(num_of_times):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            for name in range(num_of_times):
                fun(*args, **kwargs)

        return wrapper

    return decorator


@repeat(num_of_times=5)
def print_name(name):
    print(f"Printed name is: {name}")


print(print_name("komal"))


#CONVERT TO UPPER CASE
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def string1(name):
    return f"All the letters in this functiuon are converted to upper case along with argument --- ({name})"


print(string1("Komal"))

#CONVERT TO LOWER CASE
def lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()

    return wrapper


@lowercase_decorator
def string2(name):
    return f"All the letters in this function are converted to lower case along with argument --- ({name})"


print(string2("KOMAL"))

#CONVERT TO CAPITALISE CASE

def capitalise_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.capitalize()

    return wrapper


@capitalise_decorator
def string3(name):
    return f"all(only 'a' in all letters in this function are converted to capitalized and name is not changed) --- ({name})"


print(string3("KOMAL"))




#USING REPLACE DECORATOR
def replace_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(".", " ")

    return wrapper


@replace_decorator
def string4(name):
    return f"all.the..letters.of.each.words.are.REPLACED.using.this.method.and.argument.is  --- ({name})"


print(string4("KOMAL"))


#CONVERT TO TITLE CASE
def title_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.title()

    return wrapper


@title_decorator
def string3(name):
    return f"all the first letters of each words are capitalized using title method and argument is  --- ({name})"


print(string3("KOMAL"))


#CONVERT TO ISCASE
def isspace_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.isspace()

    return wrapper


@isspace_decorator
def string5(name):
    return " "


print(string5("KOMAL"))


#CONVERT TO ISALNUM
def isalnum_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.isalnum()

    return wrapper


@isalnum_decorator
def string6(name):
    return f"methodandargumentis12"


print(string6("KOMAL"))


#CONVERT TO ISDIGIT
def isdigit_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.isdigit()

    return wrapper


@isdigit_decorator
def string7(name):
    return "154454"


print(string7("KOMAL"))


#USED TO COUNT CHARACTERS
def count_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.count(" ")

    return wrapper


@count_decorator
def string8(name):
    return "This method is counting the space between these words"


print(string8("KOMAL"))

"""


#USED TO JOIN CHARACTERS
def join_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.join(" KOMAL ")  #space before and after word

    return wrapper


@join_decorator
def string9(name):
    return " This, method, is, used, to, join, the, given,letter, in, between, these, words "


print(string9("KOMAL"))
"""
#o/p---
 This, method, is, used, to, join, the, given,letter, in, between, these, words K This, method, is, used, to, join, the, given,letter, in, between, these, words O This, method, is, used, to, join, the, given,letter, in, between, these, words M This, method, is, used, to, join, the, given,letter, in, between, these, words A This, method, is, used, to, join, the, given,letter, in, between, these, words L This, method, is, used, to, join, the, given,letter, in, between, these, words 
"""


def join_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.join("KOMAL ")  #space after word

    return wrapper


@join_decorator
def string10(name):
    return " This, method, is, used, to, join, the, given,letter, in, between, these, words "


print(string10("KOMAL"))

"""
o/p---
K This, method, is, used, to, join, the, given,letter, in, between, these, words O This, method, is, used, to, join, the, given,letter, in, between, these, words M This, method, is, used, to, join, the, given,letter, in, between, these, words A This, method, is, used, to, join, the, given,letter, in, between, these, words L This, method, is, used, to, join, the, given,letter, in, between, these, words


"""


def join_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.join("KOMAL")  #withoutspace

    return wrapper


@join_decorator
def string10(name):
    return " This, method, is, used, to, join, the, given,letter, in, between, these, words "


print(string10("KOMAL"))

"""
o/p---
K This, method, is, used, to, join, the, given,letter, in, between, these, words O This, method, is, used, to, join, the, given,letter, in, between, these, words M This, method, is, used, to, join, the, given,letter, in, between, these, words A This, method, is, used, to, join, the, given,letter, in, between, these, words L



"""


#SWAP CASE
def swapcase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.swapcase()

    return wrapper


@swapcase_decorator
def string11(name):
    return " ThiS MEthod is used to swaP thE Cases UsInG SwAP CASe mEThod "


print(string11("KOMAL"))
"""
o/p---
 tHIs meTHOD IS USED TO SWAp THe cASES uSiNg sWap casE MetHOD 
"""


#ZFILL DECORATOR
def zfill_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.zfill(150)

    return wrapper


@zfill_decorator
def string12(name):
    return "This will add 0 to left side when we pass number more than string characters in it"


print(string12("KOMAL"))
"""
o/p---
 00000000000000000000000000000000000000000000000000000000000000000000This will add 0 to left side when we pass number more than string characters in it
"""


#COUNT DECORATOR
def count_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.count("count")

    return wrapper


@count_decorator
def string13(name):
    return "count This will count the number of count present in string "


print(string13("KOMAL"))
"""
o/p---
3

"""


#REPLACE DECORATOR
def count_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("count", "replace")

    return wrapper


@count_decorator
def string14(name):
    return "count This will count the number of count present in string "


print(string14("KOMAL"))
"""
o/p---
replace This will replace the number of replace present in string

"""


# STARTS WITH DECORATOR

def startswith_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.startswith("count")

    return wrapper


@startswith_decorator
def string15(name):
    return "count This will count the number of count present in string "


print(string15("KOMAL"))
"""
o/p---
True

"""


# ENDS WITH DECORATOR

def endswith_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.endswith(" string")

    return wrapper


@endswith_decorator
def string16(name):
    return "count This will count the number of count present in string"


print(string16("KOMAL"))
"""
o/p---
True

"""
