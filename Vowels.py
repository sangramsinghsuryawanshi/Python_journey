# 7. Write a Program to Count the Number of Vowels in a String
s=input("Enter n given Number: ");
cnt=0;
for i in range(0,len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        cnt+=1;
print("Count of given Vowels",cnt);
    