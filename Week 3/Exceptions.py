try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# A value error will occur when using decimals
# A ZeroDivisionError occurs when attempting to divide by zero
# By requiring a strict range of inputs, errors such as the zerodivisionerror can be avoided.
