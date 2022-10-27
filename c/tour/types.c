#include <stdio.h>
#include <stdlib.h>

int main(void ) {
    // s is always true.
    char s[] = "abc";
    if (s) {
        printf("a");
    } else {
        printf("b");
    }

    return 0;
}