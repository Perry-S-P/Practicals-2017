LOWER = 33
UPPER = 127
first = input("Please enter a character: ")
print("The ASCII code for {} is {}".format(first, ord(first)))

second = int(input("Please enter a number between 33 and 127: "))
while second < LOWER or second > UPPER:
    second = int(input("Please enter a number from {} to {}: ".format(LOWER, UPPER)))
else:
    print("The character for {} is {}".format(second, chr(second)))

characters = [33, 127, 1]
for char in characters:
    print("{} {}".format(char, chr(char)))
