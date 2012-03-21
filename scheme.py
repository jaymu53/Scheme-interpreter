def add(args):
	a = 0
	for i in args: a += float(i)
	return a
def mult(args):
	a = 1
	for i in args: a *= float(i)
	return a
def div(args):
	a = 1
	for i in args: a = float(i)/a
	return a
def boolean(symbol, args):
	if symbol == "=":
		a = float(args[0])
		for i in args:
			if float(i) != a: return False 
	if symbol == ">":
		a = float(args[0])
		for i in args[1:]:
			if float(i) >= a: 
				return False
	if symbol == "<":
		a = float(args[0])
		for i in args[1:]:
			if float(i) <= a: return False
	return True
	

op = {"+": add, "*": mult, "/": div, "=": boolean, ">": boolean, "<": boolean}
bools = ["<", ">", "="]
def parse_line(expr):
		expr = expr.replace("(", "( ")
		expr = expr.replace(")", " )")
		expr = expr.split()
		return expr
		
def evalu(expr):
	expr = parse_line(expr)
	
	funct = expr[1]
	if funct in op:
		if funct in bools:
			new = op[funct](funct, expr[2:len(expr)-1])
		else: new = op[funct](expr[2:len(expr)-1]) 
	print new
def repl():
	while True:
		a = raw_input(">>>")
		try:
			evalu(a)
		
repl()

