def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n*factorial(n-1)
i = 0
while True:
    try:  
        print(f"{i}! = {factorial(i)} \n")
        i += 1
    except RecursionError:
        print(i,' is final python cant recurse it further.')
        break