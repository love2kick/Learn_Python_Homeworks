def oddgenerator():
    i=1
    while True:
        yield i
        i+=2

gen = oddgenerator()
while True:
    print(next(gen))