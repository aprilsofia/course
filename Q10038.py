# coding: utf-8
n=input()
m=int(len(n))
i=m
for i in range(0,m):
    x1= int(n[i])-int(n[i-1])
if 1<= x1 <= (m-1):
    print('Jolly')
else:
    print('Not jolly')
