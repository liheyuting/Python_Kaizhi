# -*- coding: utf-8 -*

from sys import argv
from os.path import exists
#调用模块

script, from_file, to_file =argv
#调用函数

print "Copying from  %s to %s" %(from_file, to_file)
#输出来源和去向的文件名

#we could do these two on one line too, how?
input = open (from_file)
indata = input.read()
#定义

raw_input()

output = open (to_file,'w')
output.write(indata)
print "Alright, all done"

output.close
input.close