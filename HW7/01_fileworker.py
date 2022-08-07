from pathlib import Path

class contextmanager:
    def __init__(self, filepath="", mode="r"):
        self.filepath=filepath
        self.mode=mode

    def __enter__(self):
        try:
            if self.mode not in ["w", "a", "r"]:
                raise ValueError
        except ValueError:
            self.mode=input("Wrong mode! Try once again:")
        if self.filepath=="":
            self.filepath=input("Enter file path:")
        p=Path(self.filepath)
        try:
            if p.is_file()==True:
                file=self.filepath
                self.rd=open(file, self.mode, newline="\n")
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            self.filepath=input("File not found! Try another one:")
            p=Path(self.filepath)
            if p.is_file()==True:
                file=self.filepath
                self.rd=open(file, self.mode, newline="\n")
            else:
                raise Exception("File not found!")
        except ValueError:
            print("Wrong mode!")
        return self.rd

    def __exit__(self,*args):
        self.rd.close()

with contextmanager("newfile.txt", "a") as cm:
    cm.write('New line!')
    pass