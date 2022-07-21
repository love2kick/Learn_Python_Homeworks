chars = {}
def charcount(string):
    for i in string:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    print(chars)
string='Oh, it is python'
charcount(string)