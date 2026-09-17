#include <stdio.h>

int main() {

    int distance;

    printf("Distance to obstacle in cm: ");
    scanf("%d", &distance);

    if (distance < 20) {
        printf("STOP!\n");
    }
    else {
        printf("Move forward\n");
    }

    return 0;
}