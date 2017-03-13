LOWER = 33
UPPER = 127


def main():
    get_number()
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

def get_number(LOWER, UPPER):

    try:
        value = int(input("Enter a number (10-50): "))
    except ValueError:
        print("Enter a valid number!")
    print()