"""Scott Perry"""
name = input("What is your name?: ")
if name.strip() == "":
    name = input("What is your name?: ")
print(name[::2])

