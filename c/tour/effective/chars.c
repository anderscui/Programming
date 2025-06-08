#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    printf("char max: %d, char min: %d\n", CHAR_MAX, CHAR_MIN);
    printf("unsigned char max: %d, unsigned char min: %d\n", UCHAR_MAX, 0);
    return EXIT_SUCCESS;
}