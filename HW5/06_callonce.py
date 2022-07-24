def call_once(func):
    mem=[]
    def inner(*args):
        if len(mem)==1:
            return mem[0]
        else:
            mem.insert(0,func(*args))
            return mem[0]
    return inner

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))