#include<stdio.h>

void printsquare(double x, double y, double l) {
	printf("(% lf, % lf), % lf\n", x, y, l);
}

void TSquareFractal(double x,double y,double length,int iter){
    
    if(iter == 0) return;
    
	printsquare(x,y,length);
    
    TSquareFractal(x-length/4,y-length/4,length/2,iter-1);  //Lower left Corner
    TSquareFractal(x-length/4,y+ (3.0/4.0)*length,length/2,iter-1);  //Upper left Corner
    TSquareFractal(x+(3.0/4.0)*length,y-length/4,length/2,iter-1);  //Lower Right Corner
    TSquareFractal(x+(3.0/4.0)*length,y+(3.0/4.0)*length,length/2,iter-1);  //Upper Right Corner
	
}
int main(){

double x,y,length;
int iter;
x = 0.0;
y = 0.0;
length = 100;
iter = 2;
TSquareFractal(x,y,length,iter);

return 0;
}


// Linux, Mac: gcc task3a.c -lm -o task3a; ./task3a
// Windows: gcc task3a.c -lm -o task3a; task3a


