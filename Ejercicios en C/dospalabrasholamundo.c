#include<stdio.h>
#include<string.h>

void imprimir_palabras(const char* palabra1, const char* palabra2){
    int contador = 0;
    for (int i = 0; i < strlen(palabra1); i++){
        printf("%c", palabra1[i]);
        contador++;
    }
    for (int j = contador; j < 30 - strlen(palabra2); j++){
        printf(".");
    }
    for (int k = 0; k < strlen(palabra2); k++){
        printf("%c", palabra2[k]);
    }

}

int main(){
    char palabra1[30], palabra2[30];
    fgets(palabra1, 30, stdin);
    fgets(palabra2, 30, stdin);
    palabra1[strlen(palabra1) -1] = '\0';
    palabra2[strlen(palabra2) -1] = '\0';
    imprimir_palabras(palabra1, palabra2);
}