arr = list(map(int,input().split()))
target = int(input())
seen = {}
flag = 0
for i in range(len(arr)):
    need = target - arr[i]
    if need in seen:
        print(seen[need],i)
        flag = 1
        break
    seen[arr[i]] = i
if flag == 0:
    print("-1")