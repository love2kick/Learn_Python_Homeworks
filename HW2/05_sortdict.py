d={1:3, 2:5, 3:2, 4:9, 5:4, 6:3, "peepee":0, "poopoo":10 }
sortd={sortd:l for sortd, l in sorted(d.items(), key=lambda item:item[1])}
print(sortd)