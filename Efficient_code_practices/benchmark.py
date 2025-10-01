#!/usr/bin/env python3

import timeit

emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", 
"anna@live.com", "philipp@gmail.com"]*5

def with_loop():
    result = []
    for email in emails:
        if email.endswith("@gmail.com"):
            result.append(email)
    return result
    
def with_compre():
    return [ email for email in emails if email.endswith("@gmail.com")]

if __name__ == "__main__":

    loop_time = timeit.timeit(with_loop, number=90000000)
    comp_time = timeit.timeit(with_compre, number=90000000)


    if comp_time <= loop_time:
        print("It is better to use a list comprehension")
    else:
        print("It is better to use a loop")

    times = sorted([("loop", loop_time), ("list comprehension", comp_time)])
    print(" vs ".join(f"{name} : {time}" for name, time in times))