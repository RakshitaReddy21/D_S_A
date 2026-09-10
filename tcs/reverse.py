n=int(input())
arr = list(map(int,input().split()))
if n!=len(arr):
    print("invalid input")
else:
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
    left = 0
    right=len(result)-1
    while left<right:
        result[left],result[right]=result[right],result[left]
        left = left+1
        right=right-1
    print(*result)