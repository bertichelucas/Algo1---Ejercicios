def fact(n):
    'Dado un numero n calcula su factorial'
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

