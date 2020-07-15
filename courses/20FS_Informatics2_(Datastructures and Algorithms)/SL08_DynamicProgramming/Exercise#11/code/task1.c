#include<stdio.h>
#include<stdlib.h>

#define A_SIZE 6
#define B_SIZE 5
#define C_SIZE 20

void copyArray(int source[], int dest[], int n) {
    int i;
    for(i = 0; i < n; i++) {
        dest[i] = source[i];
    }
}

/* First and last house are neighbors, so we calculate the result two times:        */
/* Once with the first house not included and once with the last house not included */
void prepareHouseArrays(int lightBulbs[], int woFirstHouse[], int woLastHouse[], int n) {
    copyArray(lightBulbs, woFirstHouse, n);
    copyArray(lightBulbs, woLastHouse, n);

    woFirstHouse[0] = 0;
    woLastHouse[n - 1] = 0;
}

int max(int x, int y) {
    return x > y ? x : y;
}

void prepareMemoizationArray(int lightBulbs[], int m[], int n) {
    if(n >= 1) {
        m[0] = lightBulbs[0];
    }
    if(n >= 2) {
        m[1] = max(lightBulbs[0], lightBulbs[1]);
    }

    int i;
    for(i = 2; i < n; i++) {
        m[i] = -1;
    }
}

int maxIlluminationRecursiveCalculation(int lightBulbs[], int n) {
    if(n == 0) {
        return 0;
    }

    int i;
    int currentBulbs = 0;

    for(i = 0; i < n; i++) {
        if(i == 0) {
            currentBulbs = lightBulbs[0];
        } else if(i == 1) {
            currentBulbs = max(lightBulbs[0], lightBulbs[1]);
        } else { /* i>1 => more than 3 houses => Neigbors present. */
            currentBulbs = max(currentBulbs, lightBulbs[i] +
                               maxIlluminationRecursiveCalculation(lightBulbs, (i - 2) + 1));
        }
    }

    return currentBulbs;
}

int maxIlluminationRecursive(int lightBulbs[], int n) {
    int bulbsWithoutFirstHouse[n];
    int bulbsWithoutLastHouse[n];

    prepareHouseArrays(lightBulbs, bulbsWithoutFirstHouse, bulbsWithoutLastHouse, n);

    int resultWOFirst = maxIlluminationRecursiveCalculation(bulbsWithoutFirstHouse, n);
    int resultWOLast = maxIlluminationRecursiveCalculation(bulbsWithoutLastHouse, n);

    return max(resultWOFirst, resultWOLast);
}

int maxIlluminationMemoizedCalculation(int lightBulbs[], int n, int m[ ]) {

    if(n == 0) {
        return 0;
    }

    if(m[n - 1] >= 0) {
        return m[n - 1];
    }

    int currentBulbs = 0;
    if(n > 2) { /* Always the case because we prepared m */
        int i;

        for(i = 2; i < n; i++) {
            currentBulbs = max(currentBulbs, lightBulbs[i] +
                               maxIlluminationMemoizedCalculation(lightBulbs, (i - 2) + 1, m));
        }
    }
    m[n - 1] = currentBulbs;
    return currentBulbs;
}

int maxIlluminationMemoized(int lightBulbs[], int n, int m[]) {
    int bulbsWithoutFirstHouse[n];
    int bulbsWithoutLastHouse[n];

    prepareHouseArrays(lightBulbs, bulbsWithoutFirstHouse, bulbsWithoutLastHouse, n);

    prepareMemoizationArray(bulbsWithoutFirstHouse, m, n);
    int resultWOFirst = maxIlluminationMemoizedCalculation(bulbsWithoutFirstHouse, n, m);

    prepareMemoizationArray(bulbsWithoutLastHouse, m, n);
    int resultWOLast = maxIlluminationMemoizedCalculation(bulbsWithoutLastHouse, n, m);

    return max(resultWOFirst, resultWOLast);
}

int maxIlluminationDynamicCalculation(int lightBulbs[], int n) {
    if(n == 0) {
        return 0;
    }

    int m[n];
    prepareMemoizationArray(lightBulbs, m, n);
    int i;
    for(i = 2; i < n; i++) {
        int currentBulbs = -1;
        int j;
        for(j = 2; j <= i; j++) {
            currentBulbs = max(currentBulbs, lightBulbs[j] + m[(j - 2)]);
        }
        m[i] = currentBulbs;
    }

    return m[n - 1];
}

int maxIlluminationDynamic(int lightBulbs[], int n) {
    int bulbsWithoutFirstHouse[n];
    int bulbsWithoutLastHouse[n];

    prepareHouseArrays(lightBulbs, bulbsWithoutFirstHouse, bulbsWithoutLastHouse, n);

    int resultWOFirst = maxIlluminationDynamicCalculation(bulbsWithoutFirstHouse, n);
    int resultWOLast = maxIlluminationDynamicCalculation(bulbsWithoutLastHouse, n);

    return max(resultWOFirst, resultWOLast);
}

int main() {
    int testArrayA[] = {11, 4, 3, 6, 8, 9};
    int testArrayB[] = {4, 4, 4, 4, 4};
    int testArrayC[] = {13, 15, 31, 21, 9, 12, 44, 32, 12, 43, 22, 9, 11, 32, 26, 22, 21, 3, 4, 29};
    int mA[A_SIZE];
    int mB[B_SIZE];
    int mC[C_SIZE];

    printf("maxIlluminationRecursive:\n");
    printf("Array A: %d\n", maxIlluminationRecursive(testArrayA, A_SIZE));
    printf("Array B: %d\n", maxIlluminationRecursive(testArrayB, B_SIZE));
    printf("Array C: %d\n", maxIlluminationRecursive(testArrayC, C_SIZE));
    printf("\n");
    printf("maxIlluminationMemoized:\n");
    printf("Array A: %d\n", maxIlluminationMemoized(testArrayA, A_SIZE, mA));
    printf("Array B: %d\n", maxIlluminationMemoized(testArrayB, B_SIZE, mB));
    printf("Array C: %d\n", maxIlluminationMemoized(testArrayC, C_SIZE, mC));
    printf("\n");
    printf("maxIlluminationDynamic:\n");
    printf("Array A: %d\n", maxIlluminationDynamic(testArrayA, A_SIZE));
    printf("Array B: %d\n", maxIlluminationDynamic(testArrayB, B_SIZE));
    printf("Array C: %d\n", maxIlluminationDynamic(testArrayC, C_SIZE));
    return 0;
}

// Linux, Mac: gcc task1.c -o task1; ./task1
// Windows: gcc task1.c -o task1; task1
