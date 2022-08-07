class MySquareIterator(object):
    def __init__(self,list):
        self.list=list
    
    def __iter__(self):
        yield from (i**2 for i in self.list)

lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)