#include <stdio.h>

void TSquareFractal(double x, double y, double l, int i){
    if (i == 0){
        return;
    }

    printf("(%f, %f) %f", x,y,l);
    // Draw 4 squares, decrease iterator, adapt coordinates & length
    // Upper Left
    TSquareFractal(x - (l/4) ,y -(l/4) ,l/2,i-1);
    // Lower Left
    TSquareFractal(x - (l/4) ,y+ l -(l/4) ,l/2,i-1);
    // Upper Right
    TSquareFractal(x + l - (l/4) ,y -(l/4) ,l/2,i-1);
    // Lower Right
    TSquareFractal(x + l - (l/4) ,y + l -(l/4) ,l/2,i-1);

}

int main(){
    int l;
    scanf("%d", &l);
    TSquareFractal(0,0,100,l);
}
