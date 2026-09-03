def odd_sum(nums):
    sum=0
    count=0
    for i in range(len(nums)):
        if nums[i]%2==1:
            sum+=nums[i]
            count+=1
    return f"sum={sum},count={count},avg={sum/count}"
    
nums_len=int(input("enter value:"))
nums=[]
for i in range(nums_len):
    k=int(input("enter value:"))
    nums.append(k)
print(odd_sum(nums))

