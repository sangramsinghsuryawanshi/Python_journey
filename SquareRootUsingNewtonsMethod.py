number=float(input("Enter a number to find its square root: "))

guess = number/2.0
tolerance=1e-10

while abs(guess*guess-number)>tolerance:
    guess=(guess+number/guess)/2

print("The square root of{number} using Newton's method is approximately: {guess}") 
