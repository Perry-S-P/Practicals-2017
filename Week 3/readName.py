in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name appears to be: ", name)
in_file.close()
