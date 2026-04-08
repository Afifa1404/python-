
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

sum_val = a + b
difference = a - b
product = a * b

if b != 0:
    quotient = a / b
    remainder = a % b
else:
    quotient = "Undefined (division by zero)"
    remainder = "Undefined (division by zero)"

print("Sum =", sum_val)
print("Difference =", difference)
print("Product =", product)
print("Quotient =", quotient)
print("Remainder =", remainder)