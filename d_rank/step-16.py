# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A, B, C = map(int, input().split())

N = 0
N += A
N *= B
N %= C

print(N)