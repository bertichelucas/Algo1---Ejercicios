#include<stdio.h>
#include<ctype.h>

void cantidad_letras_num_espacios(char cadena[]){
    char caracter;
    int numeros = 0;
    int letras = 0;
    int espacios =0;
    for (int i = 0; cadena[i] !='\0'; i++){
        caracter = cadena[i];
        if (isalpha(caracter)){
            letras++;
        }
        else if (isdigit(caracter)){
            numeros++;
        }
        else if (isspace(caracter)){
            espacios++;
        }
    }
    printf("Numeros: %d \nLetras: %d \nEspacios: %d\n", numeros, letras, espacios);
}

int main(){
    char cadena[] = "hola que tal";
    cantidad_letras_num_espacios(cadena);
    return 0;
}