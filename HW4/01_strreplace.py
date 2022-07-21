def string_replace(oldstring):
    newstring =''
    for i in oldstring:
        if i == '\"':
            newstring+=i.replace('\"', '\'')
        elif i == '\'':
            newstring+=i.replace('\'', '\"')
        else:
            newstring+=i
    return newstring
            


print(string_replace(input('Enter a string: ')))
   