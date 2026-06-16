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


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100     



def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released >1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Tom Cruise", "Crime", 1980)
print(x)

def PrintList(the_list):
    for element in the_list:
        print(element)


PrintList(['1', 1, 'the man', "abc"])



string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")


Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")