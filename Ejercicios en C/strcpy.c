#include<string.h>
#include<stdio.h>

// DOC: Completar

void strcopy(const char *origen, char *destino) {
    int len_cadena = strlen(origen);
    for (int i = 0; i < len_cadena; i++){
    destino[i] = origen[i]; 
 }   
}

int main(){
    char cadena[1] = "";
    char destino[1] = "";
    strcopy(cadena, destino);
    printf("%s xd", destino);
    return 0;
}