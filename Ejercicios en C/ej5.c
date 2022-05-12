#include <stdio.h>
#include <assert.h>
#include <string.h>

// HACER: implementar la funcion
void borrar_espacios_consecutivos(char s[]) {
    for (int i = 0; ; i++){
        if (s[i] == '\0'){
            break;
        }
        if (s[i] == ' ' && s[i + 1] == ' '){
            int j = i + 1;
            while (s[j] != '\0'){
                s[j] = s[j + 1];
                j++;
            }
            i--;
        }
    }
}

int main(void) {
    char s[] = "A otro    perro con   ese  hueso";
    borrar_espacios_consecutivos(s);
    printf("%s\n", s);
    assert(!strcmp(s, "A otro perro con ese hueso"));
    printf("%s\n", s);
    
    // OPCIONAL: Pruebas adicionales. Sugerencias:
    // - una cadena vacía
    char t[] = "";
    borrar_espacios_consecutivos(t);
    printf("%s\n", t);
    assert(!strcmp(t, ""));
    printf("%s\n", t);
    // - una cadena que contiene solo espacios
    char r[] = "   ";
    borrar_espacios_consecutivos(r);
    printf("%s\n", r);
    assert(!strcmp(r, " "));
    printf("%s: OK\n", __FILE__);
    return 0;
}
