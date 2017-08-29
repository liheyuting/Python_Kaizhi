# -*- coding: utf-8 -*

def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return (a+b)*2

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLY %d * %d" % (a,b)
	return a*b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b

print "Let's do some math with just function"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."


divide1 = divide(iq,2)
multiply1 = multiply(weight, divide1)
subtract1 = subtract(height, multiply1)
what = add(age, subtract1)

aaa=add(2,3) + subtract(4,0) + multiply (2,5) + divide(6,3)

print "That becomes;", what, "Can you do it by hand?"

def add2(x,y):
	return x*x*y*y