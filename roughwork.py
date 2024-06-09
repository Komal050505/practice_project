powder_list = ["CORN", "MAIDA"]
water_list = ["1ml", "2ml", "3ml", "4ml", "5ml"]
sugar_list = ["1mg", "2mg", "3mg", "4mg", "5mg"]
sugarfree_list = ["SUGARFREE", "NON_SUGARFREE"]


class Cake:
    def __init__(self, powder, water, sugar=None, sugar_free=None):
        self.powder = powder
        self.water = water
        self.sugar = sugar
        self.sugar_free = sugar_free

        # Correct the user's powder choice
        if self.powder.upper() not in powder_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available options are {powder_list}")
            cond = True
            while cond:
                option = int(input("Press 1 for Corn and 2 for Maida >>"))
                if option == 1:
                    self.powder = powder_list[0]
                    cond = False
                elif option == 2:
                    self.powder = powder_list[1]
                    cond = False
                else:
                    print("Wrong choice.. available options are only 1 & 2")

        # Correct the user's water choice
        if self.water.upper() not in water_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available options are {water_list}")
            cond = True
            while cond:
                option = int(input("Press 1 for 1ml, 2 for 2ml, 3 for 3ml, 4 for 4ml, 5 for 5ml >>"))
                if option in range(1, 6):
                    self.water = water_list[option - 1]
                    cond = False
                else:
                    print("Wrong choice.. available options are only 1, 2, 3, 4, 5 only")

        # Correct the user's sugar choice if provided
        if self.sugar and self.sugar.upper() not in sugar_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available options are {sugar_list}")
            cond = True
            while cond:
                option = int(input("Press 1 for 1mg, 2 for 2mg, 3 for 3mg, 4 for 4mg, 5 for 5mg >>"))
                if option in range(1, 6):
                    self.sugar = sugar_list[option - 1]
                    cond = False
                else:
                    print("Wrong choice.. available options are only 1mg, 2mg, 3mg, 4mg, 5mg")

        # Correct the user's sugar_free choice if provided
        if self.sugar_free and self.sugar_free.upper() not in sugarfree_list:
            print(f"Huh ! This is not a good choice to bake a cake")
            print(f"Available options are {sugarfree_list}")
            cond = True
            while cond:
                option = int(input("Press 1 for SUGARFREE and 2 for NON_SUGARFREE >>"))
                if option == 1:
                    self.sugar_free = sugarfree_list[0]
                    cond = False
                elif option == 2:
                    self.sugar_free = sugarfree_list[1]
                    cond = False
                else:
                    print("Wrong choice.. available options are only 1 & 2")


# User input
powder = input("Powder: ")
water = input("Water: ")
sugar = input("Sugar: ")
sugar_free = input("SugarFree: ")

# Create Cake instance
cake1 = Cake(powder=powder, water=water, sugar=sugar, sugar_free=sugar_free)
print(f"Cake baked with powder - {cake1.powder}, water - {cake1.water}, sugar - {cake1.sugar}, sugar_free - {cake1.sugar_free}")


