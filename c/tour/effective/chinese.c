#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a = 0, b;
    char c[] = {"我是谁一二三"};
    b = printf("%s\n", c);
    printf("%d %lu\n", b, sizeof(c));

    return EXIT_SUCCESS;
}