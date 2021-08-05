def par(n):
    if n >= 2 and impar(n - 1) == True:
        return True
    return False


def impar(n):
    if n == 1:
        return True
    if n > 1 and par(n - 1) == True:
        return True
    else:
        return False

print(par(46))