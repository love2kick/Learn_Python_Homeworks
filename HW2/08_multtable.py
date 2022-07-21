a = 2 #first row
b = 4 #last row
c = 3 #first column
d = 7 #last column
print("", end="\t")
for i in range(c, d+1):
    print(i, end="\t")
print()
for i in range(a, b+1):
    print(i, end="\t")
    for j in range(c, d+1):
        print(i*j, end="\t")
    print()