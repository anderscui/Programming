#include <stdio.h>
#include <stdlib.h>

int main(void) {
    static auto a = 3;
    auto p = &a;

    return EXIT_SUCCESS;
}