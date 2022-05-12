#include<stdio.h>
#include <stdlib.h>

void imprimir_inversos(){
    int numeros[5] = {0, 0, 0, 0, 0};
    for (int i = 0; i < 5; i++){
        char numero[4];
        fgets(numero,4, stdin);
        int num = atoi(numero);
        numeros[i] = num;
    }
    for (int i = 4; i > -1; i--){
        printf("%d", numeros[i]);
    }
}

int main(){
    imprimir_inversos();
    return 0;
}