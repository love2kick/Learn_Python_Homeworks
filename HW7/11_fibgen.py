def fibgen():
    a=0
    b=1
    while True:
        yield a
        a, b = b, a+b
gen=fibgen()

while True:
    print(next(gen))