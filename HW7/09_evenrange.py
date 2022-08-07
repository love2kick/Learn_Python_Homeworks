class EvenRange:
    def __init__(self, start, end):
        self.current_index = 0
        self.evenlist=[]
        i=start
        while i != end:
            i+=1
            if i%2==0:
                self.evenlist.append(i)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        try:
            if self.current_index < len(self.evenlist):
                x = self.evenlist[self.current_index]
                self.current_index += 1
                return x
            raise StopIteration ("Index out of range!")
        except StopIteration:
            print("Index out of range!")
            raise StopIteration
            
er1 = EvenRange(7,11)
print(next(er1))
print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    print(number)
