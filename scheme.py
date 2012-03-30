import readline
variables = {}
bools = ["<", ">", "=", ">=", "<="]	
define = {}
user_def = []
class function(object):
	def __init__(self,name,var,expr):
		self.name = name
		self.var = var
		self.expr = expr 
	def execute(self,args):
		if len(args) != len(self.var):
			return
		new = str(self.expr)	
		for i in xrange(len(args)):
			new = new.replace(self.var[i], args[i])	
		return eval(new)
		
def find_var(x):
	new = []
	for i in x:
		if type(i) != list and i not in "[]":
			new += [i]
	return new
def find_expr(x):
	new = []
	for i in x:
		if type(i) == list:
			new += i
	return new
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
	new = ""
	if type(expr) != list:
		expr = parse(expr)
	while "]" in expr: expr.remove("]")
	while "[" in expr: expr.remove("[")
	funct = expr[0]
	if funct == "define":
		define[expr[1]] = function(expr[1], find_var(expr[2]), find_expr(expr[2]))
		user_def.append(expr[1])
		return
	if funct in user_def:
		return evalu(define[funct].execute(expr[1:]))
	for i in xrange(len(expr)):
		if type(expr[i]) == list:
			expr[i] = evalu(expr[i])
	if funct in op:
		if funct in bools:
			new = op[funct](funct, expr[1:])
		else:
			new =  op[funct](expr[1:]) 
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