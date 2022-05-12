// DOC: Completar
#include<stdio.h>


float promedio(float numeros[], int n) {
float prom = 0;
for(int i  = 0; i < n; i ++){
    prom += numeros[i];
}
return prom / n;
}

int main(){
    float numeros[10] = {1,2,3,4,5,6,7,8,9,10};
    int n = 10;
    float res = promedio(numeros, n);
    printf("Promedio: %.2f", res);
    return 0;
}