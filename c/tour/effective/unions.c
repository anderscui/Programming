#include <stdio.h>
#include <stdlib.h>

enum node_type {
    int_type,
    float_type,
    double_type,
    long_float_type
};

struct node {
    enum node_type type;
    union {
        int inode;
        float fnode;
        double dnode;
        long double ldnode;
    } u;
} n;

int main() {
    n.type = double_type;
    n.u.dnode = 3.14;
    return EXIT_SUCCESS;
}