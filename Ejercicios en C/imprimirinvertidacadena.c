#include <stdio.h>
#include <string.h>

#define max_largo_cadena 150
void imprimir_invertida() {
    char entrada[max_largo_cadena];

    printf("Ingrese una cadena: ");
    // File Get String
    fgets(entrada, max_largo_cadena, stdin);
    // entrada = input()
    int len = strlen(entrada);

    for (int i = len - 1; 1 >= 0; i --){
        printf('%c', entrada[i]);
    }

}