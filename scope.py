"""
SCOPE RULES:
LEGB
L - LOCAL
E - ENCLOSING
G - GLOBAL
B - BUILT IN

def f1():
    print(f"X is {x}")
f1()
x = 100
# ERROR - b/c x define after the function definition

x = 100
def f1():
    print(f"X is {x}")
f1()
# OUTPUT : X is 100

# GLOBAL
x = 100
y = 200
def f1():
    x = 300
    y = 400
    print(f"X is {x}")
    print(f"Y is {y}")
f1()
# OUTPUT
X is 300
Y is 400

# L E G B
# GLOBAL
x = 100
y = 200

def f1():
    x = 300 # F1 local varible x
    print(f"Inside f1 X is {x}") # 300
    print(f"Inside f1 Y is {y}") # y is not a local variable b/c y is not defined
def f2():
    print(f"Inside f2 X is {x}") # f2 nearest function is f1 so check name x in
    print(f"Inside f2 Y is {y}") # Look up check in f2 fun -> f1 -> Global
f2()
f1()
# OUTPUT
Inside f1 X is 300
Inside f1 Y is 200
Inside f2 X is 300
Inside f2 Y is 200

# L E G B
# GLOBAL
x = 100
y = 200
def f1():
    x = 300 # F1 local varible x
    y = 0 # F1 local varible y
    print(f"Inside f1 X is {x}") # 300
    print(f"Inside f1 Y is {y}") # Look up Local - 0
def f2():
    print(f"Inside f2 X is {x}") # f2 nearest function is f1 so check name x in
    print(f"Inside f2 Y is {y}") # Look up check in f2 fun -> f1 # 0
f2()
f1()
# OUTPUT
Inside f1 X is 300
Inside f1 Y is 0
Inside f2 X is 300
Inside f2 Y is 0

# L E G B
# GLOBAL
x = 100
y = 200
def f1():
    print(f"Inside f1 X is {x}")
    print(f"Inside f1 Y is {y}")

def f2():
    print(f"Inside f2 X is {x}")
    print(f"Inside f2 Y is {y}")
f2()
f1()
# OUTPUT
Inside f1 X is 100
Inside f1 Y is 200
Inside f2 X is 100
Inside f2 Y is 200

# L E G B
# GLOBAL
x = 100
y = 200
def f1():
    x = 400
    print(f"Inside f1 X is {x}") # 400
    print(f"Inside f1 Y is {y}") # 200
def f2():
    global x
    print(f"Inside f2 X is {x}") # Please look x value in global space - 100
    print(f"Inside f2 Y is {y}") # 200
f2()
f1()
# OUTPUT
Inside f1 X is 400
Inside f1 Y is 200
Inside f2 X is 100
Inside f2 Y is 200

# GLOBAL
x = 100
y = 200
def f1():
    x = 400
    print(f"Inside f1 X is {x}") # 400
    print(f"Inside f1 Y is {y}") # 200
def f2():
    global x

    print(f"Inside f2 X is {x}") # Please look x value in global space - 100
    print(f"Inside f2 Y is {y}") # 200
f2()
f1()
print(f"Global x is {x}") # 100
print(f"Global y is {y}") # 200
# OUTPUT
Inside f1 X is 400
Inside f1 Y is 200
Inside f2 X is 100
Inside f2 Y is 200
Global x is 100
Global y is 200

# GLOBAL
x = 100
y = 200
def f1():
    x = 400
    print(f"Inside f1 X is {x}") # 400
    print(f"Inside f1 Y is {y}") # 200
def f2():
    global x # Look x value in Global scope
    x = 700 # Dangerous b/c it overwrites the global x value from 100 to 700
    print(f"Inside f2 X is {x}") # Global x is updated 700
    print(f"Inside f2 Y is {y}") # Global 200
f2()
f1()
print(f"Global x is {x}") # 700
print(f"Global y is {y}") # 200

"""

# GLOBAL
x = 100
y = 200
num_list = [10, 20, 30, 40]
print(f"Minimum number is {min(num_list)}")  # Look up Local -> Enclosing -> Global ->#Minimum number is 10
print(f"Max number is {max(num_list)}")  # Max number is 40


def f1():
    x = 400

    print(f"Inside f1 X is {x}")  # 400
    print(f"Inside f1 Y is {y}")  # 200


def f2():
    global x  # Look x value in Global scope
    x = 700  # Dangerous b/c it overwrites the global x value from 100 to 700
    print(f"Inside f2 X is {x}")  # Global x is updated 700
    print(f"Inside f2 Y is {y}")  # Global 200


f2()
f1()
print(f"Global x is {x}")  # 700
print(f"Global y is {y}")  # 200
"""
Minimum number is 10
Max number is 40
Inside f2 X is 700
Inside f2 Y is 200
Inside f1 X is 400
Inside f1 Y is 200
Global y is 200
"""


def f3():
    global x
    x = "a"
    print(f"Inside f3 X is {x}")
    global y
    y = "b"
    print(f"Inside f3 Y is {y}")


f3()
print(f"Global x in f3() is {x}")
print(f"Global y in f3() is {y}")

num_list1 = [10, 20, 30, 40, 10.1, 50.5, 9, 0.1, 265956565]
print(f"Minimum number is {min(num_list1)}")
print(f"Max number is {max(num_list1)}")


def f4():
    num_list2 = [10, 20, 30, 40, 10.1, 50.5, 9, 0.1, 265956565, 52, 64]
    global x
    print(f"Inside f4 X is {x}")
    print(f"Inside f4 Y is {y}")
    print(f"Num_list is {num_list2}")
    print(f"minimum value from the num_list is : {min(num_list2)}")
    print(f"maximum value from the num_list is : {max(num_list2)}")
    print(f"Sum of the  values from the num_list is : {sum(num_list2)}")
    print(f"Length of the values from the num_list is : {len(num_list2)}")
    print(f"Average of the values from the num_list is : {sum(num_list2) / len(num_list2)}")


f4()

"""
Num_list is [10, 20, 30, 40, 10.1, 50.5, 9, 0.1, 265956565, 52, 64]
minimum value from the num_list is : 0.1
maximum value from the num_list is : 265956565
Sum of the  values from the num_list is : 265956850.7
Length of the values from the num_list is : 11
Average of the values from the num_list is : 24177895.518181816


"""


def f5():
    global x
    print(f"global x is {x}")
    x = x + "b"
    print(f"x is {x}")
    global y
    y = y + "a"
    print(f"y is {y}")


f5()
print(f"x + y from f5() is {x + y}")


def f6():
    str_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    print(f"str_list is {str_list}")
    print(f"max(str_list) is {max(str_list)}")
    print(f"min(str_list) is {min(str_list)}")
    print(f"len(str_list) is {len(str_list)}")


f6()
"""
str_list is ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max(str_list) is j
min(str_list) is a
len(str_list) is 10



"""
x = 50
y = 70


def f7():
    global x
    print(f"Before changing x value Inside f7 X is {x}")

    x = 55
    print(f"After changing global x value Inside f7 X is {x}")

    global y
    print(f"Before changing global y value Inside f7 Y is {y}")
    y = 55555
    print(f"After changing global y value Inside f7 Y is {y}")


f7()

"""

Before changing x value Inside f7 X is 50
After changing global x value Inside f7 X is 55
Before changing global y value Inside f7 Y is 70
After changing global y value Inside f7 Y is 55555
"""
x = 100
y = 1000


def f8():
    x = 400

    print(f"Inside f8 X is {x}")  # 400
    print(f"Inside f8 Y is {y}")  # 200


f8()


def f9():
    print(f"Inside f9 X is {x}")  # Global x is updated 700
    print(f"Inside f9 Y is {y}")  # Global 200


f9()

"""


Inside f8 X is 400
Inside f8 Y is 1000
Inside f9 X is 100
Inside f9 Y is 1000


"""