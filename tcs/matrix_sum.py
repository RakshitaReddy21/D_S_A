n = int(input())
trace = 0
for i in range(n):
    row = list(map(int,input().split()))
    trace += row[i]
print(trace)