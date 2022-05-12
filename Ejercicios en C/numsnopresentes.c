#include <stdio.h>
void numsnopresentes(int numeros[], int lennum, int ignorar[], int lenign){
    for (int i = 0; i < lennum; i++){
        for (int j = 0; j < lenign; j++){
            if (numeros[i] == ignorar[j]){
                break;
            }
            else if (j == lenign -1){
                printf("%d\n", numeros[i]);
            }
        }
    }
}

int main(){
    int numeros[] = {1,2,7,2,3,5};
    int ignorar[] = {2,3};
    numsnopresentes(numeros, 6, ignorar, 2);
    return 0;
}