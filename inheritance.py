class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Lion details created")
        print("\n")
        print(f"Lion name: {self.name}")
        print(f"Lion age: {self.age}")


class Lionness(Lion):
    def __init__(self, gender, powerful, name, age):
        self.powerful = powerful
        self.gender = gender
        print(f"Lionness details created")
        print("\n")
        print(f"Lionness gender: {self.gender}")
        print(f"Lionness powerful: {self.powerful}")
        print(f"Deriving from Lion class started...")
        super().__init__(name=name, age=age)


class Cub(Lionness):
    def __init__(self, qualities):
        self.qualities = qualities
        print(f"Cub details created")
        print("\n")
        print(f"Cub quality: {self.qualities}")
        print(f"Deriving from Lionness class started...")
        super().__init__(gender="female", powerful="powerful", name="lion", age=5)


result_object = Cub("Super")
print(f"Cub is having the qualities of --- {result_object.qualities}")
print(f"Cub is having the age of --- {result_object.age}")
print(f"Cub is having the gender of --- {result_object.gender}")
print(f"Cub is having the name of --- {result_object.name}")
print(f"Cub is having the powerful of --- {result_object.powerful}")
