import sys

def after_10_year(age):
    return f"After ten years, You will be {age+10} years old.\nLife is too short :("


if __name__ == "__main__":
    age = sys.argv
    if len(age) != 2:
        raise Exception("What!! you forgot your age???")
    
    print(after_10_year(int(age[1])))