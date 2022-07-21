def splitstring(oldstring, split_char):
    splitlist = []
    currentstr=""
    for i in oldstring:
        if i == split_char:
            splitlist.append(currentstr)
            currentstr=""
        else:
            currentstr+=i
    splitlist.append(currentstr)
    return splitlist

print(splitstring('Currently i\'m learning python, it\'s pretty hard, i feel no regret',','))