def char_all(*args):
    setlist=[]
    for i in args:
        setlist.append(set(i))
    let=tuple(sorted(set.intersection(*setlist)))
    return let
        

def all_chars(*args):
    setlist=[]
    for i in args:
        setlist.append(set(i))
    let=tuple(sorted(set.union(*setlist)))
    return let

def chars_in_two(*args):
    setlist=[]
    let=[]
    for i in args:
        setlist.append(set(i))
    for f, s1 in enumerate(setlist[:-1]):
        for j, s2 in enumerate(setlist[f+1:]):
            let.append(set.intersection(s1,s2))
    let=tuple(sorted(set.union(*let)))
    return let

def others(*args):
    setlist=[]
    for i in args:
        setlist.append(set(i))
    let=sorted(set.union(*setlist))
    alphabet=list(map(chr, range(ord('a'), ord('z')+1)))
    others=[]
    for i in alphabet:
        if i not in let:
            others.append(i)
    return tuple(others)

test_strings = ["hello", "world", "python", ]
print(char_all(*test_strings))
print(all_chars(*test_strings))
print(chars_in_two(*test_strings))
print(others(*test_strings))