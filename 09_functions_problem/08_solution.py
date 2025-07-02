# FUNCTION WITH **KWARGS
    # Create a function that accepts any number of keyboard arguments and prints them in the format key:value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="walt", power="chemistry")
print_kwargs(name="walt")
print_kwargs(name="walt", power="chemistry", enemy="Mexican Brothers")