#include <stdio.h>
#include <stdlib.h>

void swap(int *, int *);

int main() {
    int a = 21;
    int b = 17;
    swap(&a, &b);
    printf("main: a = %d, b = %d\n", a, b);
    return EXIT_SUCCESS;
}

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
    printf("swap: a = %d, b = %d\n", *a, *b);
}