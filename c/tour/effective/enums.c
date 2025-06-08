#include <stdio.h>
#include <stdlib.h>

enum day { sun, mon, tue, wed, thu, fri, sat };
enum cardinal_points { north = 0, east = 90, south = 180, west = 270 };

enum seasons: unsigned short {
    spring = 1,
    summer,
    autumn,
    winter
};

int main() {
    enum day today = 9;
    printf("today is %d\n", today);
    return EXIT_SUCCESS;
}