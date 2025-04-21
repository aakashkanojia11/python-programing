
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division to avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined"

print("Addition:  ",addition)
print("Subtraction: ",subtraction)
print("Multiplication: ",multiplication)
print("Division: ",division)
