#include<stdio.h>
#include <stdlib.h>

void adivinar(int numero){
    int contador = 0;
    int num = 0;
    while(num > numero || num < numero){
        contador++;
        char intento[4];
        fgets(intento,4, stdin);
        int num = atoi(intento);
        printf("%d", num);
        if (num > numero){
            printf("El numero ingresado es mayor al numero oculto\n");
        }
        else if (num < numero){
            printf("El numero ingresado es menor al numero oculto\n");
        }
        else if (num == numero){
            printf("intento : %d", contador);
            break;
        }
    }
}

int main(){
    int numero = 7;
    adivinar(numero);
}