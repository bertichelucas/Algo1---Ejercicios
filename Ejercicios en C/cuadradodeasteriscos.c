
// Implementar una funcion que recibe un numero entero N(positivo) e imprime un cuadrado de *
// de lado N (solo el borde)
#include<stdio.h>


void imprimir_cuadrado(int n){
    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == 0 || i == n -1){
            printf("*");
            }
            else if (j == 0 ||  j == n - 1){
            printf("*");
            }
            else {
            printf(" ");
            }
        }
    printf("\n");
    }
}

int main(){
    imprimir_cuadrado(5);
    return 0;
}