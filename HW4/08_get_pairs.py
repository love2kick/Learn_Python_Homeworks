def get_pairs(lst: list) -> list[tuple]:
    if len(lst)==1:
        return None
    else:
        elist=[]
        for i in range(len(lst)-1):
            t=[lst[i], lst[i+1]]
            elist.append(tuple(t))
        return elist

print(get_pairs([1]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1, 2, 3, 8, 9]))