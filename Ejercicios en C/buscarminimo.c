#include<stdio.h>
// si el minimo esta repetido devuelve la posicion de la primera aparicion
int buscar_minimo(int arreglo[], int cant){
    int posicion = 0;
    int minimo = arreglo[0];
    for(int i = 0; i < cant; i ++) {
        if(arreglo[i] < minimo){
            minimo = arreglo[i];
            posicion = i;
        }   
    }
    return posicion;
}

int main(){
    int arreglo[10] = {9,67,33,22,-11,0,55,13,-23,17};
    int cant = 10;
    int res = buscar_minimo(arreglo, cant);
    printf("La posicion es %d", res);
    return 0;
}