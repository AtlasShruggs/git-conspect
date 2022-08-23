from signal import SIG_DFL


print('Hello world!')
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(8))


a, b, c = [3] * 3

print(a+b+c)

total = [i for i in range(5)]

print(total)