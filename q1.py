

def factorial(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f

x = int(input())

fact = factorial(x)

print(fact)



