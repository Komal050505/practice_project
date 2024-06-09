#looping items in given list
list = [1, 2, 4, 5, 6, 7, 8, 9, 10]
for item in list:
    print(item)
#---------------------------------------------------------------------


#range function

for num in range(5):
    print(num)
# ---------------------------------------------------------------------


#to get date and time
from datetime import datetime

current_datetime = datetime.now()

print(f"Current date and time is :- {current_datetime}")
#---------------------------------------------------------------------


# printing even nums
num = [1, 2, 3, 4, 5, 6]

sum_even_num = 0

for item in num:

    if item % 2 == 0:
        sum_even_num += item

print(f"Sum of even numbers is :{sum_even_num}")
#---------------------------------------------------------------------





#---------------------------------------------------------------------


#functipon with sample example
def sample_add():
    a = 5
    b = 10
    sum = a + b
    return sum


print(f"function with sample_add example is {sample_add()}")


#---------------------------------------------------------------------

#class
class SampleClass:
    def __init__(self):
        self.a = 5
        self.b = 10
        self.sum = self.a + self.b
        print(self.sum)


#obj creation for sample class
obj = SampleClass()
print(f"accessing constructor class attribute and value of attribute is - {obj.a}")
print(f"accessing constructor class attribute and value of attribute is - {obj.b}")
print(f"accessing constructor class attribute and value of sum attribute(a+b) is - {obj.sum}")
#---------------------------------------------------------------------


#inheritance
class Animal_Parent:
    def __init__(self,name):
        self.name = name
class Animal_Child(Animal_Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
obj = Animal_Child( name='tiger', age=5)

print(f"Inheritance -- name: {obj.name}, age: {obj.age}")
#--------------------------------------------------------------------

# nested if
num = 5
if num == 5:
    print("num = 5")
    if num >= 1:
        print("num > 1")
        if num <= 4:
            print("true")
        else:
            print("false")

#---------------------------------------------------------------------


# countdown timer
"""
import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Remaining time is: {seconds} seconds")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


countdown_duration = 5
countdown_timer(countdown_duration)

"""

#range using step
for item in range(1, 100, 5):
    print(item)
#---------------------------------------------------------------------
