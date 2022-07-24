def sort_list(file):
    x=[]
    output=open("./data/sorted_names.txt", "w")
    for i in open(file).readlines():
        x.append(i[:-1])
    for j in sorted(x):
        j=j+'\n'
        output.write(j)

sort_list("./data/unsorted_names.txt")