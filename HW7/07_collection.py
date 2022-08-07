class MyNumberCollection(object):
    def __init__(self, start, end=10, step=1):
        self.collist=[]
        if type(start)==int:
            self.collist.append(start)
            for i in range(start,end,step):
                if i not in self.collist:
                    self.collist.append(i)
            self.collist.append(end)
        else:
            for i in start:
                try:
                    if type(i)!=int:
                        raise TypeError
                    else:
                        self.collist.append(i)
                except TypeError:
                    print("MyNumberCollection supports only integers!")

    def __str__(self) -> str:
        return str(self.collist)

    def __getitem__(self, index):
        return self.collist[index]**2

    def append(self,number):
        try:
            if type(number)!=int:
                raise TypeError
            else:
                self.collist.append(int(number))
        except TypeError:
            print(f"{number} is a {type(number)}, not an integer!")
        finally:
            return str(self.collist)

    def __add__(self,other):
        for i in other:
            self.collist.append(int(i))
        return self.collist

    def __radd__(self,other):
        for i in other:
            self.collist.append(int(i))
        return self.collist

    def __iter__(self):
        yield from self.collist

col1 = MyNumberCollection(0, 5, 2)
print(col1)
col2 = MyNumberCollection((1,2,3,4,5,))
print(col2)
col3 = MyNumberCollection((1,2,3,"4",5))
col1.append(7)
col1.append("something")
print(col2[4])
print(col1 + col2)
for item in col1:
    print(item)
