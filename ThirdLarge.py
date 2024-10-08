# 8. Write a Python Program to Find the Largest of Three Numbers
a=int(input("Enter First Number: "));
b=int(input("Enter Second Number: "));
c=int(input("Enter Third Number: "));
if a>b and a>c :
    print("a is Greater than b and c");
elif b>a and b>c:
     print("b is Greater than b and c");
else:
     print("c is Greater than b and a");