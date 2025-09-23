import os
import sys

class Add_nubers():
    def __init__(self, path, file_line):
        if not os.path.isfile(path):
            raise Exception("Faylda xato bor...")
        self.path = path
        self.line = file_line

    def read_and_add(self):
        with open(self.path, "r") as file:
            lines = file.readlines()
            
            if not lines:
                raise Exception("Fayl nega bo'sh -_-")
            if not len(lines) >= self.line:
                raise Exception("Qator xato kiritilgan 0.0")
            add = 0
            for i in range(int(self.line)):
                line = lines[i].strip().split()
                for a in line:
                    if line != "":
                        add+=int(a)
            return add

if __name__ == "__main__":
    malumot = sys.argv
    if len(malumot)!=3:
        raise Exception("Nimadir yoki nimadirlar qolib ketti yoo aa")
    ad = Add_nubers(malumot[1], int(malumot[2]))
    print(ad.read_and_add())    