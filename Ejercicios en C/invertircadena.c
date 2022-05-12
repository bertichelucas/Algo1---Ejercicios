#include<stdio.h>
#include<string.h>

void invertir (char* s){
    int len_cadena = strlen(s);
    for(int i = 0; i < len_cadena / 2; i++){
        char aux = s[i];
        s[i] = s[len_cadena -1 - i];
        s[len_cadena - 1 -i] = aux;
    }
}

int main() {
    char cadena[10] ="0123456789";
    invertir(cadena);
    printf("%s", cadena);
    return 0;
}