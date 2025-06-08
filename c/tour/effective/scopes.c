#include <stdio.h>
#include <stdlib.h>

int j; // file j begins

void f(int i) {  // block i begins
    int j = 1;   // block j begins
    i++;         // refer to param
    for (int i = 0; i < 2; ++i) {  // block - local i begins
        int j = 2;                 // block - inner j begins
        printf("%d\n", j);
    }  // block - local i and block - inner j ends
    printf("%d\n", j);  // outer j, 1
}  // block i, j ends

void g(int j); // func prototype scope j.

int main() {
    printf("the value is %d\n", j);
    return EXIT_SUCCESS;
}