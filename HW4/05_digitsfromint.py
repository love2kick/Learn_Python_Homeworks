def get_digits(num: int) -> tuple[int]:
    templist = []
    for i in str(num):
        templist.append(int(i))
    return tuple(templist)

def get_digits2(num: int) -> tuple[int]:
    return tuple(map(int, str(num)))

print(get_digits(87178291199))
print(get_digits2(87178291199))