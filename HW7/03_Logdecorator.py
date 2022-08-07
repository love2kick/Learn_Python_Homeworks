from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

def timelogger(func):
    def inner(*args, **kwargs):
        logpath="./log/logfile.log"
        if Path(logpath).is_file()==False:
            f=open(logpath,"w",newline="\n")
        else:
            f=open(logpath,"a",newline="\n")
        currenttime = datetime.now(timezone.utc)
        f.write(f"{func.__name__} starts at {currenttime}.\n")
        e=func(*args, **kwargs)
        f.write(f"{func.__name__} ends at {currenttime}.\n")
        return e
    return inner

@timelogger    
@contextmanager
def fileworker(file="newfile2.txt", mode="a"):
    try:
        if mode not in ["w", "a"]:
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
    f.write(1)
