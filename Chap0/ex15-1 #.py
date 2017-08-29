# -*- coding: utf-8 -*
from sys import argv

#定义
script, filename = argv

#txt定义为open 函数
txt = open (filename)

#print 文件名以及 文件内容
print "Here's your file %r:" % filename
print txt.read()

#再次，可以由用户输入文件名，print 文件名以及内容
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()