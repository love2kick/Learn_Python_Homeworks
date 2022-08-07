class CustomError(Exception):
    pass

def even(number:str):
    try:
        if number==None:
            number=str(input("Input a number to check:"))
        elif int(number)<=3:
            print("Number too small!")
            raise CustomError("Number too small!")
        elif number.isalpha()==True:
            print("Not a Number!")
            raise CustomError("Not a Number!")
        elif int(number) % 2 != 0:
            print("Not even number!")
            raise CustomError("Not even number!")
    except (Exception, CustomError):
        number=str(input("Input number again:")) 
    finally:
        if int(number) % 2 == 0:
            return int(number)