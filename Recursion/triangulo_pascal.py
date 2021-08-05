def pascal(n, k):
    #Triangulo de pascal. https://es.wikipedia.org/wiki/Tri%C3%A1ngulo_de_Pascal
    if  k == 0 or k == n:
        return 1
    return pascal(n- 1, k) + pascal(n - 1, k - 1)


 
    
