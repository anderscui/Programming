#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct sig_record {
    int signum;
    char signame[20];
    char sigdesc[100];
} sigline, * sigline_p;

int main() {
    sigline.signum = 5;
    strcpy(sigline.signame, "SIGINT");
    strcpy(sigline.sigdesc, "Interrupt from keyboard");

    sigline_p = &sigline;
    sigline_p->signum = 10;

    return EXIT_SUCCESS;
}