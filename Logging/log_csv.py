import logging
import csv
import os


class Name_age:
    def input_name_age():
        with open("date.csv", "a", newline="") as file:
            write = csv.writer(file)
            if os.stat("date.csv").st_size==0:
                write.writerow(["Name", "Age"])
            while True:
                ism_yosh = list(map(str,input("Ism va yosh kiriting(Agar to'xtatmoqchi bo'lsangiz enter ni bosin):").split()))
                if len(ism_yosh) != 2 or len(ism_yosh) ==0:
                    break
                else:
                   write.writerow([ism_yosh[0], ism_yosh[1]])
    def log_read(file):
    
        logging.info("log_read() funksiyasi ishlashni boshladi.")
        if not os.path.isfile(file):
            logging.error("File topilmadi")
            raise Exception("Fayl topilmadi")
        
        with open(file, "r") as fayl:
            lines = fayl.readlines()
            name = []
            for line in lines[1:]:
                age = line.strip().split(",")
                if age[1].isdigit():
                    logging.info(f"{age[0]} da yosh to'g'ri")
                else:
                    logging.warning(f"{age[0]} da yosh to'g'ri emas")
                name.append(age[0])
            return "\n".join(name)


if __name__ == "__main__":
    logging.basicConfig (
        filename="date.log",
        level = logging.DEBUG,
        format = "%(asctime)s - %(message)s",   
        datefmt = "%Y-%m-%d %H:%M:%S"
    )
    Name_age.input_name_age()
    print(Name_age.log_read("date.csv"))


