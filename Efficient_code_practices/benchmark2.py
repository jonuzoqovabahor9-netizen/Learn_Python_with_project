#!/usr/bin/env python3

import sys
import timeit

emails = [
    "john@gmail.com", "james@gmail.com", "alice@yahoo.com",
    "anna@live.com", "philipp@gmail.com"
] * 5


def with_loop():
    result = []
    for email in emails:
        if email.endswith("@gmail.com"):
            result.append(email)

    return result

def with_comp():
    return [email for email in emails if email.endswith("@gmail.com")]


def with_map():
    return list(map(lambda e :e if e.endswith("@gmail.com") else None, emails))

def with_filter():
    return list(filter(lambda email: email.endswith("@gmail.com"), emails))

if __name__ == "__main__":
    if len(sys.argv) <3:
        print("Look: ./benchmark.py <function_name> <number_of_calls>")
        sys.exit(1)
    
    func_name = sys.argv[1]
    number = sys.argv[2]

    funcs  = {
        "loop": with_loop,
        "list_comprehension":with_comp,
        "map":with_map,
        "filter":with_filter
    }

    if func_name not in funcs:
        print(f"Funksiya topilmadii ")
        sys.exit(1)

    func = funcs[func_name]
    time = timeit.timeit(func, number=int(number))
    print(time)