# -*- coding: utf-8 -*

#加入function
from sys import argv

#调用函数
script, input_file =argv

#define 三个函数
#定义读取
def print_all(f):
	print f.read()

#读取值多少
def rewind(f):
	f.seek(0)

#读取字节数
def print_a_line(line_count,f):
	print line_count, f.readline()

#current——file设置为打开input_file
current_file = open (input_file)

#读取input_file
print_all(current_file)

#打印一句话
print "Now let's rew, kind of like a tape."
rewind(current_file)

#打印
print "Let's print three lines:"
 
#多读一行，输出
current_line = 1
print_a_line(current_line, current_file)

#多读一行，输出
current_line += 1
print_a_line(current_line, current_file)

#多读一行，输出
current_line += 1
print_a_line(current_line, current_file)