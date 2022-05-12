
#include<string.h>
#include<stdio.h>
void inicializar_arreglo_vacio(int numeros[], int len){
    for(int i = 0; i < len; i++){
        numeros[i] =0;
    }
}

void contar_apariciones(char* cadena,int numeros[], int len){
    int len_cadena = strlen(cadena);
    for (int i = 0; i < len_cadena; i ++){
        int caracter = cadena[i];
        numeros[caracter]++;
    }
}

void imprimir_arreglo(int numeros[], int len){
    for(int i = 0; i < len; i++){
        if (numeros[i] > 0){
            printf("%c, %d", i, numeros[i])
;        }
    }
}

void imprimir_apariciones(char* cadena){
    int numeros[256];
    inicializar_arreglo_vacio(numeros, 256);
    contar_apariciones(cadena, numeros, 256);
    imprimir_arreglo(numeros, 256);
}

int main(){
    imprimir_apariciones("Barbara");
    return 0;
}