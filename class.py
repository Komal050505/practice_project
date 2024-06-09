"""
# Variable # Attribute
name = "John Doe"

# Function # Method
def audio_feature():
    pass
# OOPS
Class - Blueprint which has attributes and methods
object - It is a instance of a class using this object you can access attribute and me
SYNTAX:
class <class_name>:
<attributes>
<methods>

class Simple:
    pass
obj = Simple()
print(f"Simple is {Simple}")
print(f"Object is {obj}")

class Simple:
    name = "John Doe"
    age = 45
obj = Simple()
print(f"Simple is {Simple}")
print(f"Object is {obj}")
print("\nAccessing the attributes of the class using object")
print(f"Access the name -{obj.name}")
print(f"Age the name -{obj.age}")
# OUTPUT:

Accessing the attributes of the class using object
Access the name -John Doe
Age the name -45

class Cake:
    sugar = "500Kg"
    powder = "Corn powder"
    def step1(self):
        return f"Mix the powder with adequate water"
    def step2(self):
        return f"Add sugar"
cake1 = Cake()
cake2 = Cake()
print(f"Accessing attributes........")
print(f"Accessing sugar attribute using the cake1 object - {cake1.sugar}")
print(f"Accessing powder attribute using the cake1 object - {cake1.powder}")
print(f"Accessing methods........")
print(f"Step1 method accessing way is 'cake1.step1()' and it returned '{cake1.step1()}
print(f"Step1 method accessing way is 'cake2.step1()' and it returned '{cake2.step1()}

OUTPUT:
Accessing attributes........
Accessing sugar attribute using the cake1 object - 500Kg
Accessing powder attribute using the cake1 object - Corn powder
Accessing methods........
Step1 method accessing way is 'cake1.step1()' and it returned 'Mix the powder with adeq
Step1 method accessing way is 'cake2.step1()' and it returned 'Mix the powder with adeq

class SimpleConstructor:
    def __init__(self): # THis will be invoked/called while creating an
        print(f"I called by default")
sc = SimpleConstructor()
# Initilise the attribute

class SimpleConstructor:
    def __init__(self, name):
        self.name = name # self.name is instance attribute - LIFE TIME IS every
        age = 45 # Normal attribute - LIFE TIME is within the function
    def get_name(self):
        return f"Get name method returned {self.name}"
    def get_age(self):
    return f"Age is {age}"
sc = SimpleConstructor("John Doe")
print(f"Accessing the attributes .......")
print(f"'self' is instance reference here instance is 'sc' so i directly do 'sc.name'
# print(f"Accessing age using sc is {sc.age}") # ERROR as age is normal variable
print(f"Access the age using 'get_age' method {sc.get_age()}")




class SimpleConstructor:
    def __init__(self, name):
        self.name = name
        self.age = 45

    def get_name(self):
        return f"Get name method returned {self.name}"

    def get_age(self):
        return f"Age is {age}"


sc = SimpleConstructor("John Doe")
print(f"Accessing the attributes .......")
print(f"'self' is instance reference here instance is 'sc' so i directly do 'sc.name'")
# print(f"Accessing age using sc is {sc.age}") # ERROR as age is normal variable
print(f"Access the age using 'get_age' method {sc.get_age()}")



class SimpleConstructor:
    def __init__(self, name, age):
        self.name = name  # Instance attribute reference - so availability is within c
        self.age = age  # # Instance attribute reference - so availability is within cl

    def get_name(self):
        return f"Get name method returned {self.name}"

    def get_age(self):
        return f"Age is {self.age}"


def audio():
    print(f"Audio")


sc = SimpleConstructor("Komal", 27)
print(f"Accessing the instance attributes 'name' and 'age'")
print(f"Person name is {sc.name}")
print(f"Person age is {sc.age}")
print(f"Accessing the methods ..")
print(f"'get_name' method calling like this and returned is '{sc.get_name()}'")
print(sc.audio())

"""

"""
class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free


cake1 = Cake(powder="Corn", water="0.5ml")
print(f"powder -{cake1.powder}")
print(f"Water -{cake1.water}")
print(f"Sugar -{cake1.sugar}")
print(f"Sugar Free -{cake1.sugar_free}")
"""
"""
OUTPUT:
powder -Corn
Water -0.5ml
Sugar -None
Sugar Free -None
"""

"""
class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free


cake1 = Cake(powder="Corn", water="0.5ml")
cake2 = Cake(powder="Chilli", water="0.1ml", sugar="10gm")
print(f"{cake2.powder}")
print(f"{cake2.water}")
print(f"{cake2.sugar}")
print(f"{cake2.sugar_free}")
"""
"""
OUTPUT:
Chilli
0.1ml
10gm
None
"""

"""
class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free


cake1 = Cake(powder="Corn Strong", water="0.5ml")
print(f"Cake1 powder - {cake1.powder}")  # "Corn Strong
cake2 = Cake(powder="Chilli", water="0.1ml", sugar="10gm")
print(f"Cake2 powder - {cake2.powder}")  # "Chilli
# Updating the object attribute
cake2.powder = "Corn Weak"
print(f"Cake2 powder after overwriting - {cake2.powder}")
print(f"Cake1 powder - {cake1.powder}")
"""
"""
Output:
Cake1 powder - Corn Strong
Cake2 powder - Chilli
Cake2 powder after overwriting - Corn Weak
Cake1 powder - Corn Strong
"""

"""
class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free


cake1 = Cake(powder="Corn Strong", water="0.5ml")
print(f"Cake1 powder - {cake1.powder}")  # "Corn Strong
del cake1
cake2 = Cake(powder="Chilli", water="0.1ml", sugar="10gm")
print(f"Cake2 powder - {cake2.powder}")  # "Chilli
# Updating the object attribute
cake2.powder = "Corn Weak"
print(f"Cake2 powder after overwriting - {cake2.powder}")
#print(f"Cake1 powder - {cake1.powder}") # ERROR because we have deleted cake1 in previous steps

"""
"""
OUTPUT:
Cake1 powder - Corn Strong
Cake2 powder - Chilli
Cake2 powder after overwriting - Corn Weak

"""
"""

class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free


cake1 = Cake(powder="Corn Strong", water="0.5ml")
print(f"Cake1 powder - {cake1.powder}")  # "Corn Strong
del cake1
cake2 = Cake(powder="Chilli", water="0.1ml", sugar="10gm")
print(f"Cake2 powder - {cake2.powder}")  # "Chilli
# Updating the object attribute

cake2.powder = "Corn Weak"
print(f"Cake2 powder after overwriting - {cake2.powder}")


#print(f"Cake1 powder - {cake1.powder}")  # ERROR because we have deleted cake1


class Cake:
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free
        if self.sugar_free == '':
            print("User entered incorrect value for sugar free ")
            self.sugar_free = None


# USER enters these from the keyboard
powder = input("powder:")  # Corn
water = input("Water:")  # 2l
sugar = input("Sugar:")  # 3gm
sugar_free = input("SugarFree:")  # ''
cake1 = Cake(powder=powder, water=water, sugar=sugar, sugar_free=sugar_free)
print(f"Cake baked with powder -{cake1.powder} water -{cake1.water}Sugar {cake1.sugar} SugarFree {cake1.sugar_free} ")
"""
"""
OUTPUT:
powder:Corn
Water:2l
Sugar:3gm
SugarFree:
User entered incorrect value for sugar free
Cake baked with powder -Corn water -2l Sugar 3gm SugarFree None
"""

# Task: Correct the chef mistake while baking the cake
powder_list = ["CORN", "MAIDA"]
water_list = ["1ml", "2ml", "3ml", "4ml", "5ml"]
sugar_list = ["1mg", "2mg", "3mg", "4mg", "5mg"]
sugarfree_list = ["SUGARFREE", "NON_SUGARFREE"]


class Cake:
    # --------------------------Cake class block Started ----------------------
    # Attributes
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        # ------------------Attributes Section Started---------------------
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free
        # ------------------Attributes Section Ended---------------------
        print(f"powder value is {powder}")
        print(f"powder is {self.powder} and type is {type(self.powder)}")  # )
        print(f"Cond is {self.powder.upper() not in powder_list}")
        # --------------------- Correct the user water choice Block Started------------
        if self.water.upper() not in water_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available option is {water_list}")
            print(f"Choose your choice... ")
            cond = True
            while cond == True:  # Infinity loop that breaks with valid user choice
                option = int(input("Press 1 for 1ml, 2 for 2ml, 3 for 3ml, 4 for 4ml, 5 for 5ml >>"))
                if option == 1:
                    self.water = water_list[0]
                    cond = False
                if option == 2:
                    self.water = water_list[1]
                    cond = False
                if option == 3:
                    self.water = water_list[2]
                    cond = False
                if option == 4:
                    self.water = water_list[3]
                    cond = False
                if option == 5:
                    self.water = water_list[4]
                    cond = False
                    print("Wrong choice.. available options are only 1,2,3,4,5 only")
            #----------------------Correct the user water choice Block Ended-------------------------
        # --------------------- Correct the user powder choice Block Started------------
        if self.powder.upper() not in powder_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available option is {powder_list}")
            print(f"Choose your choice... ")
            cond = True
            while cond == True:  # Infinity loop that breaks with valid user choice
                option = int(input("Press 1 for Corn and 2 for Maida>>"))
                if option == 1:
                    self.powder = powder_list[0]
                    cond = False
                if option == 2:
                    self.powder = powder_list[1]
                    cond = False
                    print("Wrong choice.. available options are only 1 & 2")
                # --------------------- Correct the user powder choice Block Ended----------------
                # --------------------- Correct the user sugar choice Block Started----------------
                if self.sugar.upper() not in sugar_list:
                    print(f"Huh ! This is not a good choice to bake a cake")
                    print(f"Available option is {sugar_list}")
                    print(f"Choose your choice... ")
                    cond = True
                    while cond == True:  # Infinity loop that breaks with valid user choice
                        option = int(input("Press 1 for 1mg, 2 for 2mg, 3 for 3mg, 4 for 4mg, 5 for 5mg >>"))
                        if option == 1:
                            self.sugar = sugar_list[0]
                            cond = False
                        if option == 2:
                            self.sugar = sugar_list[1]
                            cond = False
                        if option == 3:
                            self.sugar = sugar_list[2]
                            cond = False
                        if option == 4:
                            self.sugar = sugar_list[3]
                            cond = False
                        if option == 5:
                            self.sugar = sugar_list[4]
                            cond = False
                            print("Wrong choice.. available options are only 1mg, 2mg, 3mg, 4mg, 5mg ")
                    # --------------------- Correct the user sugar choice Block Ended----------------
                print(f"sugar_free value is {sugar_free}")
                print(f"sugar_free is {self.sugar_free} and type is {type(self.sugar_free)}")  # )
                print(f"Cond is {self.sugar_free.upper() not in sugarfree_list}")
                # --------------------- Correct the user sugar_free choice Block Started------------
                if self.sugar_free.upper() not in sugarfree_list:
                    print(f"Huh ! This is not a good choice to bake a cake")
                    print(f"Available option is {sugarfree_list}")
                    print(f"Choose your choice... ")
                    cond = True
                    while cond == True:  # Infinity loop that breaks with valid user choice
                        option = int(input("Press 1 for sugar_free and 2 for non_sugar_free>>"))
                        if option == 1:
                            self.sugar_free = sugarfree_list[0]
                            cond = False
                        if option == 2:
                            self.sugar_free = sugarfree_list[1]
                            cond = False
                            print("Wrong choice.. available options are only 1 & 2")
                        # --------------------- Correct the user sugar_free choice Block Ended-------------

                # --------------------------Cake class block End ----------------------


# USER enters these from the keyboard


powder = input("powder:")
water = input("Water:")
sugar = input("Sugar:")
sugar_free = input("SugarFree:")
cake1 = Cake(powder=powder, water=water, sugar=sugar, sugar_free=sugar_free)
print(f"Cake baked with powder -{cake1.powder} water -{cake1.water} Sugar {cake1.sugar} SugarFree {cake1.sugar_free} ")
