#include<stdio.h>
#include<string.h>


void vocales_asteriscos(char* cadena, int len){
    char vocales[5] = {'a', 'e', 'i', 'o', 'u'};
    for (int i =0; i < len; i++){
        for (int j = 0; j < 5; j++){
           if (cadena[i] == vocales[j]){
               i++;
               j =0;
               printf("*");
           }
        }
        printf("%c", cadena[i]);
    }
}

int main(){
    printf("Ingrese una cadena: ");
    char cadena[200]; 
    fgets(cadena, 200, stdin);
    int len = strlen(cadena);
    cadena[strlen(cadena) -1] = '\0';
    vocales_asteriscos(cadena, len);
    return 0;
}