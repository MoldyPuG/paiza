n = int(input())
a_list = list(map(int, input().split()))
k = int(input())

order_num = 0

for i in range(0, n):
    if a_list[i] == k:
        order_num = i+1

print(order_num)