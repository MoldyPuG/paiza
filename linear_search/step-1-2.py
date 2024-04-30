n = int(input())
a_list = list(map(int, input().split()))
k = int(input())

for i in range(0, n):
    if a_list[i] == k:
        print(i+1)
        break
    elif i == n-1:
        print(0)