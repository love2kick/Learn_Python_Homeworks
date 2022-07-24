import operator
import csv

def get_top_performers(file_path, number_of_top_students=5):
    csvfile=open(file_path,'r', newline="")
    rdr = csv.reader(csvfile)
    next(rdr, None)
    l = sorted(rdr, key=lambda x: float(x[2]), reverse=True)
    toplist=[i[0] for i in l[0:number_of_top_students]]
    return toplist

print(get_top_performers("./data/students.csv"))

def studsort(file_path):
    csvfile=open(file_path,'r', newline="")
    rdr = csv.reader(csvfile)
    next(rdr, None)
    l = sorted(rdr, key=lambda x: int(x[1]), reverse=True)
    with open('./data/students_sorted.csv','w', newline='') as w:
        write=csv.writer(w)
        header=['student name','age','average mark']
        write.writerow(i.strip() for i in header)
        write.writerows(l)

studsort("./data/students.csv")