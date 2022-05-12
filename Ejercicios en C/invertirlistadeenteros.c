#include<stdio.h>

void invertir(int* lista, int cant){
    int aux;
    for(int i = 0; i < cant/2; i++){
    aux = lista[i];
    lista[i] = lista[cant - i - 1];
    lista[cant - i - 1] = aux;
    };
}

int main() {
    int notas[10] = {1,2,3,4,5,6,7,8,9,10};
    int cant = 10;
    invertir(notas, cant);
    for(int i = 0; i < cant; i++){
        printf("%d", notas[i]);
    }
    
}