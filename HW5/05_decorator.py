def remember_result(func):
	mem=[]
	def inner(*args):
		if len(mem)==0:
			print(f"Previous result = 'None'")
			mem.insert(0,func(*args))
		elif len(mem)==1:
			print(f"Previous result = '{mem[0]}'")
			mem.insert(1,func(*args))
		else:
			print(f"Previous result = '{mem[0]}'")
			mem.insert(0,mem[1])
			mem.insert(1,func(*args))
	return inner 
	
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += str(item)
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)