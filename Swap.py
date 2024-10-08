# 1. Write a Program to Swap Two Numbers Without Using a Temporary Variable
a=int(input("Enter First Number: "));
b=int(input("Enter Second Number: "));
print(a , " ", b);
a=a+b;
b=a-b;
a=a-b;
print(a , " ", b);