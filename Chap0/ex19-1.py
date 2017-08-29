# -*- coding: utf-8 -*

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
#定义cheese_and_crackers 函数，含有两个参数，输出三句话

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#设置函数的参数为（20，30）

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#定义两个字符串分别等于的数值

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#赋值函数的两个参数为两个定义后的字符串

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#输出（10+20，5+6）后的函数值对应的三句话

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)
#输出（参数+100，参数2+1000）后的函数值对应的三句话


def apple(count):
	print "You have %d apple!" % count

apple(1)
a=5
apple(a)
apple(a+5)
apple(a*2)
apple(a*a)
apple(a+a*2)

apple(6+2)

aa=3
apple(aa+a)

aaa=a+aa
apple(aaa)

apple(a+aa+aaa)