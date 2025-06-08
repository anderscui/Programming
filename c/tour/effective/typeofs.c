#include <stdio.h>
#include <stdlib.h>

const _Atomic int asi = 0;
const int si = 0;

const char* const beatles[] = {
        "John",
        "Paul",
        "George",
        "Ringo",
};

typeof_unqual(si) main(void) {
    typeof_unqual(asi) plain_si;
    typeof(_Atomic typeof(si)) atomic_si;

    typeof(beatles) beatles_array;
    typeof_unqual(beatles) beatles2_array;

    return EXIT_SUCCESS;
}