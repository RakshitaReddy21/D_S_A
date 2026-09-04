n=int(input("enter value:"))
temp = n
rev=0
while n>0:
    digit=n%10
    rev = rev*10+digit
    n=n//10
if (rev==temp):
    print("palindrome")
else:
    print("not palindrome")