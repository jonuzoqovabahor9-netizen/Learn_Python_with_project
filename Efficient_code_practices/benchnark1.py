#!/usr/bin/env python3

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
    return list(map(lambda email:email.endswith("@gmail.com"), emails))

if __name__ == "__main__":

    loop_time = timeit.timeit(with_loop, number=1000000)
    comp_time = timeit.timeit(with_comp, number=1000000)
    map_time = timeit.timeit(with_map, number=1000000)

    if map_time <= comp_time and map_time <= loop_time:
        print("It is better to use a map")
    elif comp_time <= loop_time and comp_time <= map_time:
        print("It is better to use a comprehension")
    else:
        print("It is better to use a loop")

    times = sorted([("loop", loop_time), ("map", map_time), ("list comprehension", comp_time)], key= lambda x: x[1])

    print(" vs ".join(f"{name}: {time}" for name, time in times))

