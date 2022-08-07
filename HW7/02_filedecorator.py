from contextlib import contextmanager

@contextmanager
def fileworker(file="newfile2.txt", mode="a"):
    try:
        if mode not in ["w", "a", "r"]:
            raise ValueError
        else:
            f = open(file, mode, newline="\n")  
            yield f
    except PermissionError:
        print("File permission denied!")
    except ValueError:
        print("Incorrect mode, try 'w' or 'a'!")   
    finally:
        f.close()
    

with fileworker() as f:
    f.write("Hello people!")
