def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# Example usage
num1 = 56
num2 = 98

print(gcd(num1, num2))
