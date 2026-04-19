def factorial(n):
    result = 1
    i = 1

    while i <= n:
        result = result * i
        i = i + 1
    return result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    i = 2

    while i <= n:
        result = result * i
        i = i + 1

    return result

print(factorial(0))  
print(factorial(1))  
print(factorial(5))  
