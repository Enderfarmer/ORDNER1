

def print_new():
    print("new")

def is_even_or_odd(number):
    """Prints even if divided by 2 otherwise odd."""
    assert number.type() in [int, float]
    if number % 2== 0:
        print("even")
    else:
        print("odd")

    
x =1
is_even_or_odd(x)

x = 2
is_even_or_odd(x)


x = 4
is_even_or_odd(x)
