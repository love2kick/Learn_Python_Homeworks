class counter:

    def __init__(self):
        num=int
    
    def increment(self, start=0, max_value=int):
        self.num=start
        while self.num!=max_value:
            self.num+=1
        if self.num==max_value:
            print("Maximal value is reached.")

    def get(self):
        print(self.num)
        return self.num

c = counter()
c.increment(42,100)
c.get()