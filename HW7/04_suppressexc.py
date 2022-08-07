from contextlib import contextmanager, suppress
from datetime import datetime, timezone
def sup(func):
    def inner(*args):
        with suppress(Exception):
            currenttime = datetime.now(timezone.utc)
            print(f"{func.__name__} starts at {currenttime}.\n")
            func(*args)
            print(f"{func.__name__} ends at {currenttime}.\n")
        return inner

@contextmanager
def fileworker(file="newfile2.txt", mode="a"):
    try:
        f = open(file, mode, newline="\n")  
        yield f 
    finally:
        f.close()

with fileworker() as f:
    f.write("1")