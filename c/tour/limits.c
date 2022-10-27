#include <stdio.h>
#include <limits.h>

#define ABS(i) ((i) < 0 ? -(i) : (i))

int main(void ) {
    printf("uint max = %u\n", UINT_MAX);
    printf("int max = %d\n", INT_MAX);
    printf("int min = %d\n", INT_MIN);

    // wraparound
    unsigned int ui = UINT_MAX;
    ui++;
    printf("ui max + 1 = %u\n", ui);
    ui--;
    printf("ui min - 1 = %u\n", ui);

    // overflow
    signed int si = INT_MIN;
    signed int abs_si = ABS(si);
    signed int abs_si_2 = ABS(si+1);
    printf("abs of int min = %d \n", abs_si);
    printf("abs of int min + 1 = %d \n", abs_si_2);

    // float std
#if defined(__STDC_IEC_559__)
    println("Annex F: defined");
#else
    printf("Annex F: undefined");
#endif

    signed char c;
    int i = INT_MAX;
    long k;
    k = (c = i);

    return 0;
}
