#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_big(int);

int main() {
    int num = 1000;
    bool is_big_num = is_big(num);
    printf("%d is a big number: %d\n", num, is_big_num);
    return EXIT_SUCCESS;
}

bool is_big(int n) {
    return n > 100;
}