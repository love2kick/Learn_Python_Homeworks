def foo(l: list[int]) -> list[int]:
    multlist=[]
    result=1
    for i in l:
        result=result*i
    for j in l:
        multlist.append(int(result/j))
    return multlist

print(foo([1,2,3,4,5]))