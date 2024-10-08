# 6. Write a Program to Check if a String is a Palindrome
s=input("Enter n given Number: ");
s1=''.join(reversed(s));
if s==s1:
    print("Given String palindrome");
else:
    print("Given String is not Palindrome");
    