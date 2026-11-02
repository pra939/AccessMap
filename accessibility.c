#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    if (argc != 4) {
        printf("Invalid input!");
        return 1;
    }

    int ramp = atoi(argv[1]);
    int lift = atoi(argv[2]);
    int toilet = atoi(argv[3]);

    if ((ramp != 0 && ramp != 1) ||
        (lift != 0 && lift != 1) ||
        (toilet != 0 && toilet != 1)) {

        printf("Enter only 0 or 1!");
        return 1;
    }

    int score = 0;

    if (ramp == 1)
        score += 40;

    if (lift == 1)
        score += 30;

    if (toilet == 1)
        score += 30;

    printf("Accessibility Score: %d/100\n", score);

    if (score >= 80)
        printf("Highly Accessible");

    else if (score >= 50)
        printf("Moderately Accessible");

    else
        printf("Needs Improvement");

    return 0;
}