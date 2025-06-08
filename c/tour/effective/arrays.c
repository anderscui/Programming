#include <stdio.h>
#include <stdlib.h>

int main() {
    char str[11];  // allocate sufficient storage (10+1)
    for (unsigned int i = 0; i < 10; ++i) {
        str[i] = '0' + i;
    }
    str[10] = '\0';
    printf("digits: %s\n", str);
    return EXIT_SUCCESS;
}