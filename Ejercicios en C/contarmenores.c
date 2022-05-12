#include<stdio.h>

int contar_menores(int numeros[], int len, int valor) {
    int resultado = 0;
    for (int i = 0; i < len; i++){
        if (numeros[i] < valor){
            resultado++;
        }
    }
    return resultado;
}

int main(){
    int numeros[] = {1,2,3,4,5,6,7,8,9,10};
    int len = 10;
    int valor = 5;
    int res = contar_menores(numeros, len, valor);
    printf("Hay %d numeros menores", res);
    return 0;
}