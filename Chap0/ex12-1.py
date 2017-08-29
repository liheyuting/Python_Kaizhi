# -*- coding: utf-8 -*
age = raw_input("How old are you?")
height = raw_input("How old are you?")
weight = raw_input("How old are you?")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

#raw_input(...)
#raw_input([prompt]) -> string   
#Read a string from standard input.  The trailing newline is stripped.
#If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#On Unix, GNU readline is used if enabled.  The prompt string, if given, is printed without a trailing newline before reading.
