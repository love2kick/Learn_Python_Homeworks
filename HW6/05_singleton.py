class Sun:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sun, cls).__new__(cls)
        return cls.instance
        
p = Sun()
f = Sun()
print(p is f)