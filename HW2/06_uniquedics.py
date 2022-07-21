dlist=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
uniquev=set(i for l in dlist for i in l.values())
uniquel=[]
for i in uniquev:
    uniquel.append(i)
print(uniquel)