import sys
import csv

class Save_name_age:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        with open("name.csv", mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow([self.name,self.age])
        return "Faylga qo'shildi"

if __name__ == "__main__":
    malumot = sys.argv
    if len(malumot) != 3:
        raise Exception("You need enter file name , name and age")
    ss = Save_name_age(malumot[1].title(), malumot[2])
    print(ss.save())

                       