import sys

def hello(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    name=sys.argv
    if len(name)!= 2:
        raise Exception("What happened??You forgot name or file -_-")
    print(hello(name[1].title()))
