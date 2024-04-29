# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
a_list = list(map(int, input().split()))
k = int(input())

count = 0

for i in range(len(a_list)):
    if a_list[i] == k:
        count += 1

print(count)