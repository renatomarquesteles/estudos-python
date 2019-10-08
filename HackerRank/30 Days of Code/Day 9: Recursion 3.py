def factorial(n):
    if n > 1:
        res = n * factorial(n-1)
        return res
    else:
        return 1


n = int(input())
print(factorial(n))