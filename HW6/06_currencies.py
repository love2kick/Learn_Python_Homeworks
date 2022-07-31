from functools import total_ordering
import numpy as np

class Money:
    currency_amount=float
    currency_type=str
    def __init__(self,*args):
        self.exchange_rate = {
                "EUR": 0.93,
                "BYN": 2.1,
                "JPY": 130.84,
                "BTC": 21567.5
                }
        if len(args)==1:
            self.currency_type="BTC"
            self.currency_amount=self.exchange_rate.get('BTC')*args[0]
            self.ret=[self.currency_type,self.currency_amount]
        else:
            self.currency_type=args[1]
            self.currency_amount=self.exchange_rate.get(args[1])*args[0]
            self.ret=[self.currency_type,self.currency_amount]
        
    def __repr__(self):
        return f"Currency:{self.currency_type}"

    def __add__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount + other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount + other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __radd__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount + other)
                    /self.exchange_rate.get(self.ret[0]))
        if type(self)==tuple:
            return ((self.currency_amount + other[0])
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount + other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __mul__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount * other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount * other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __rmul__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount * other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount * other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __sub__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount - other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount - other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __rsub__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount - other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount - other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __div__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount / other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount / other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    def __rdiv__(self, other)->float:
        if type(other)==float or int:
            return ((self.currency_amount / other)
                    /self.exchange_rate.get(self.ret[0]))
        else:
            return ((self.currency_amount / other.currency_amount)
                    /self.exchange_rate.get(self.ret[0]))
    
x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”