#include<math.h>

void map(int entrada[], int salida[], int len) {
    int salida[len];
    for(int i = 0; i < len; i++){
        double cuadrado = pow(entrada[i], 2);
        salida[i] = cuadrado;
    }
}

// como no se puede devolver un arreglo por ahora
// lo que se hace es recibir el arreglo de salida por parametro
// para poder mutarlo
