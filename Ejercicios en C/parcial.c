#include<stdio.h>
#include<stdlib.h>


void pedir_numero(){
    int arreglo[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    char caracter[2];
    while (1){
        printf("Ingrese un numero del 0 al 9\n");
        fgets(caracter, 2, stdin);
        int numero = atoi(caracter);
        printf("%d\n", numero);
        if (0<=numero && numero <=9){
            arreglo[numero]++;
        }
    }
    for (int i = 0; i < 10; i++){
        printf("%d : se escribio %d veces\n", i, arreglo[i]);
        }   
}

int main(){
    pedir_numero();
    return 0;
}