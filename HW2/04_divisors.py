def finddevisors(i):
    devlist=[]
    for n in range(1, i+1):
        if i%n==0:
            devlist.append(n)
    print(devlist)
    
finddevisors(i=int(input("Enter your number:")))