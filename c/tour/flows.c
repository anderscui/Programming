#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef enum { Savings, Checking, MoneyMarket} AccountType;

bool safeDiv(int dividend, int divisor, int *quotient) {
    if (!quotient) {return false;}
    if ((divisor == 0) || ((dividend == INT_MIN) && (divisor == -1))) {return false;}

    *quotient = dividend / divisor;
    return true;
}

void showGrade(unsigned int marks) {
    switch (marks / 10) {
        case 10:
        case 9:
            puts("your grade: A");
            break;
        case 8:
            puts("your grade: B");
            break;
        case 7:
            puts("your grade: C");
            break;
        default:
            puts("your grade: F");
            break;
    }
}

void showInterestRate(AccountType account) {
    double interest_rate;
    switch (account) {
        case Savings:
            interest_rate = 3.0;
            break;
        case Checking:
            interest_rate = 1.0;
            break;
        case MoneyMarket:
            interest_rate = 4.5;
            break;
        // for detecting future new values.
        default: abort();
    }
    printf("interest rate = %g.\n", interest_rate);
}

int main(void ) {
    int quotient;
    bool is_safe = safeDiv(INT_MIN, -1, &quotient);
    if (is_safe) {
        printf("safe div: quotient = %d \n", quotient);
    } else {
        printf("unsafe div \n");
    }

    showGrade(91);
    showGrade(59);

    showInterestRate(Savings);

    return 0;
}