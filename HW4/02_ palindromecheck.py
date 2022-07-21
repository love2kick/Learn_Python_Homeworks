def palicheck(string):
    string = string.replace(" ", "")
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False

print(palicheck(input('Enter a string: ')))