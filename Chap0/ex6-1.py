#定义x
x="There are %d types of people." %10
#定义binary
binary = "binary"

#定义“do_not)
do_not = "don't"
#定义y把变量放进去了
y = "Those who know %s and those who %s" %(binary, do_not)

#输出x和y
print x
print y

#输出 我说过的话
print "I said: %r" % x
print "I also said: '%s'. " % y

#两个定义
hilarious =False
joke_evaluation = "Isn't that joke so funny?! %r" 

#打印
print joke_evaluation % hilarious

#定义w和e
w = "This is the left side of ..."
e = "a string with a right a right side."

#输出两个的和
print w+e 

#因为两个字母代表都是字符串，加起来更长