"""
a = 10
b = 2.5
c = "Hello"
print(type(a), type(b), type(c))

x = "123"
y = 45.67
print(int(x))
print(int(y))

s = "Python Programming"
#get = s.split()
#print(get[0])
print(s.upper())
print(s.replace("Programming", "language"))

s = "Hello, World!"
print(s[7])
print(s[-1])
print(s[0:5])

lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)
lst.remove(3)
print(lst)
lst.reverse()
print(lst)

lst = [1, 2, 3, 4, 5]
lst[2] = 10
print(lst)

d = {"name": "John", "age": 25, "city": "New York"}
d["email"] = "john@example.com"
print(d)
d["age"] = 26
print(d)
d.pop("city")
print(d)


d = {"a": 1, "b": 2, "c": 3}
print(d["b"])
d["d"] = 4
print(d)

t = (1, 2, 3, 4, 5)
print(t[2])
print(t[1:4])
if 3 in t:
    print(f"3 is in tuple {t}")
else:
    print(f"3 is not in tuple {t}")


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"intersection - {set1 & set2}")
print(f"union - {set1 | set2}")
is_subset = set1.issubset(set2)
print(f"is s1 subset of s2 - {is_subset}")


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)
"""

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
#print(sc.audio())