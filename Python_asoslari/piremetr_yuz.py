def kvadrat_a():
    a = int(input("Kvadrat tomonini kiriting:"))
    return a
def primetr_yuz(a):
    return f"Kvadratning yuz {a*a} ga teng.\nPerimetri esa {a*4} ga teng."

if __name__ == "__main__":
    a = kvadrat_a()
    print(primetr_yuz(a))