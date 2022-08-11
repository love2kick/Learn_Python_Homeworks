import os
class CustomError(Exception):
    pass

def even(number):
    try:
        if str(number).isdigit()==False:
            print("Not a Number!")
            raise CustomError("Not a Number!")
        elif int(number)<=3:
            print("Number too small!")
            raise CustomError("Number too small!")
        elif int(number) % 2 != 0:
            print("Not even number!")
            raise CustomError("Not even number!")
    except (CustomError):
        number=input("Input number again:")
    finally:
        if int(number) % 2 == 0 and int(number) > 3:
            return True, int(number)
        else:
            raise CustomError("Wrong input!")

def eratosthenes(n):
    primes = list (range(2, n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

def odd_primes(n):
    oddprimes = eratosthenes(n)
    oddprimes.remove(2)
    return oddprimes

def goldbach():
    n=input("Enter number:")
    x, y = 0, 0
    result = 0
    ifeven=even(n)
    if ifeven[0] == True:
        n=ifeven[1]
        prime = odd_primes(n)
        while result != n:
            for i in range(len(prime)):
                if result == n: break 
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == n: break 
    print(x, y)
    os.system("pause")
    return x, y