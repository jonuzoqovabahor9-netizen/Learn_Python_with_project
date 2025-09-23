import sys

def operations_on_numbers( n1, n2):
    ishoralar = ['+','-','*',":"]
    javoblar = [n1+n2,n1-n2,n1*n2, n1/n2]
    for i in range(4):
        print(f"{n1} {ishoralar[i]} {n2} = {javoblar[i]}")

if __name__ == "__main__":
    numbers = sys.argv
    if len(numbers) != 3:
        raise Exception("What?? Why are forgot that 00")
    operations_on_numbers(int(numbers[1]), int(numbers[2]))
