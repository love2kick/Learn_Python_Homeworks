def generate_squares(num:int):
    d={}
    for i in range(1,num+1):
        d.update({i:i**2})
    return d

print(generate_squares(5))