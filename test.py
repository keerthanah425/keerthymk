def myFunction():# This is function definition
    print("Hello There")


    def add(a):
       """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

help(add)
add(1)
add(2)

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

Mult(2, 3)
Mult(10.0, 3.14)
Mult(2, "Michael Jackson ")


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
f = fib
f(100)