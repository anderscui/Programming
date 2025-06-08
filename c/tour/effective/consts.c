#include <stdio.h>
#include <stdlib.h>

int main() {
    const int i = 1;
    // error: cannot assign to variable 'i' with const-qualified type 'const int'
    // i = 2;

    // convince the compiler to change a const var.
    int *ip = (int *)&i;
    *ip = 2;  // undefined behavior
    printf("const value: %d, pointed value: %d\n", i, *ip);
    return EXIT_SUCCESS;
}