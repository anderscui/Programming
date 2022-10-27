#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char c[10];
    int i;
    double d;
} widget;

void showWidget(widget *pw) {
    printf("i = %d, d = %f, c = %s \n", pw->i, pw->d, pw->c);
}

int main(void ) {
    // malloc
    printf("size of widget: %lu\n", sizeof(widget));
    widget *pw = malloc(sizeof(widget));
    if (pw == NULL) {
        printf("malloc failed.");
    } else {
        pw->i = 1;
        pw->d = 2.0;
    }

    // void type
    void *pw2 = malloc(sizeof(widget));
    widget w = {"abc", 9, 3.2};
    // have a effective type after memcpy.
    memcpy(pw2, &w, sizeof(widget));
    showWidget(pw2);

    // alloc string value
    char *str = (char *)(malloc(16));
    if (str) {
        strncpy(str, "123456789abcdef", 15);
        str[15] = '\0';

        printf("str = %s\n", str);
        free(str);
        return EXIT_SUCCESS;
    } else {
        return EXIT_FAILURE;
    }

    return 0;
}