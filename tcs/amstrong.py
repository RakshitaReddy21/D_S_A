n=int(input("enter value:"))
temp=n
p=len(str(n))
sum=0
while n >0:
    digit=n%10
    sum = sum +digit **p
    n=n//10
if(sum == temp):
    print("armstrong")
else:
    print("not armstrong")