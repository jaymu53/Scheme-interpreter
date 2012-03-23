import readline
variables = {}
def add(args):
	return reduce(lambda x, y: float(x) + float(y), args)

def sub(args):
	return reduce(lambda x, y: float(x) - float(y), args)

def mult(args):
	return reduce(lambda x, y: float(x) *float(y), args)

def div(args):
	return reduce(lambda x, y: float(x) / float(y), args)

def boolean(symbol, args):
	a = float(args[0])
	if symbol == "=":
		return len(filter(lambda x: float(x) != a, args[1:])) == 0
	elif symbol == ">":
		return len(filter(lambda x: float(x) >= a, args[1:])) == 0
	elif symbol == "<":
		return len(filter(lambda x: float(x) <= a, args[1:])) == 0


def print_var(args):
	print len(args)
	if len(args) == 1:
		if eval(args[0]) == str or eval(args[0]) == int or eval(args[0]) == float:
				return args[0]
	else: 
		return "Incorrect input"

def setVar(var, val):
	variables[var] = val
	return
op = {"+": add, "*": mult, "/": div, "=": boolean, ">": boolean, "<": boolean, "print": print_var, "-": sub}
bools = ["<", ">", "=", ">=", "<="]	


def parse(a):
	new = []
	if type(a) != list:
		a = a.replace("(", " [ ").replace(")"," ] ")
		a = a.strip()
		a = a.split()
	if "[" not in a[1:]: 
		return a
	for i in xrange(len(a)):
		if a[i] == "[" and i != 0:
			new += [parse(a[i:])]
			return new
		else: 
			
			new += [a[i]]
	return new

def evalu(expr):
	if type(expr) != list:
		expr = parse(expr)
	while "]" in expr: expr.remove("]")
	while "[" in expr: expr.remove("[")
	funct = expr[0]
	var = None
	if funct == "set!":
			var = expr[1]
			expr = expr[2:]
			
	for i in xrange(len(expr)):
		if type(expr[i]) == list:
			expr[i] = evalu(expr[i])
	if funct in op:
		if funct in bools:
			new = op[funct](funct, expr[1:])
		else: new = op[funct](expr[1:]) 
	return new

def repl():
	while True:
			a = raw_input(">>>") 
			if a == "exit": break
			try:
				print evalu(a)
			except: 
				print "error"
repl()
