formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (formatter,formatter,formatter,formatter)
print formatter %(
	"I had this thing",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#错误都记录在学习笔记中
#先计算单引号，再计算双引号