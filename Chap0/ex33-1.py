#!usr/bin/env python
# _*_ coding:utf-8 _*_

i=0

numbers = []
m = int (input("number1:"))
n = int(input("number2:"))

if i < n:
    print("At the top i is %d" %m)
    numbers.append(i)
    i=i+m
    print("Numbers now:", numbers)
    print("At the bottom i is %d" %i)
else:
        exit(0)


print("The numbers:")

for num in numbers:
    print(num)
