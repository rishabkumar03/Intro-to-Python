# FUNCTION WITH *ARGS
    # Write a function that takes variable number of arguments and return their sum.

def total_sum(*args):
    print(args)
    for i in args:
        print(i)
    return sum(args)

print(total_sum(1, 2, 3))