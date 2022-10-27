#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

bool is_odd(int n) {
    // do not use != 1 because of the negative nums (C use truncating division, with any fractional part discarded).
    return n % 2 != 0;
}

int main(void ) {
    int i = 0;
    int j = 0;

    j += ++i+1;
    printf("j = %d \n", j);

    // precedence
    char abc[] = "abc";
    char xyz[] = "xyz";

    char *p = abc;
    // ++*p -> ++(*p)
    printf("%c", ++*p);

    p = xyz;
    // *p++ -> *(p++)
    printf("%c\n", *p++);

    // undefined behavior
    i = 5;
    printf("result = %d \n", i++ * i++);

    // sizeof
    int a;
    size_t a_size = sizeof a;
    size_t int_size = sizeof(int) * CHAR_BIT;

    printf("%zu, %zu \n", a_size, int_size);

    // remainders
    printf("10/3 = %d\n", 10/3);
    printf("10/-3 = %d\n", 10/-3);
    printf("-10/3 = %d\n", -10/3);
    printf("-10/-3 = %d\n", -10/-3);

    // boolean
    printf("is_odd(1) = %d\n", is_odd(1));
    printf("is_odd(1) = %d\n", is_odd(-1));

    // too-far pointer
    int m[3] = {1, 2, 3};
    int *pi;
    j = 0;
    for (pi = &m[0]; pi < &m[3]; ++pi) {
        j += *pi;
    }
    printf("sum of array: %d \n", j);

    return 0;
}
