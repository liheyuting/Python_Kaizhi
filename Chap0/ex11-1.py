# -*- coding: utf-8 -*
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#test 1 
record = []
while True:
  info = []
  userInput = raw_input('Enter something: ')
  if userInput == "exit":
    break
  else:
    info=userInput.split(",")
    record+=[info]
print record


#test by self
print "Hello, what's your name",
name2=raw_input()
print "Congratulation，%r，geme over" % name2