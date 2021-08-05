def collatz(n):
    #Conjetura de Collatz.
    #https://es.wikipedia.org/wiki/Conjetura_de_Collatz
    print(n)
    if n == 1:
        return 
    if n % 2 == 0:
        return collatz(n / 2)
    if n % 2 != 0:
        return collatz(n * 3 + 1)
