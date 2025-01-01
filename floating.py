# Accept three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the absolute value of each number
abs1 = abs(num1)
abs2 = abs(num2)
abs3 = abs(num3)

# Add the absolute values
result = abs1 + abs2 + abs3

# Display the result with float representation
print(f"The sum of the absolute values is: {result:.2f}")
