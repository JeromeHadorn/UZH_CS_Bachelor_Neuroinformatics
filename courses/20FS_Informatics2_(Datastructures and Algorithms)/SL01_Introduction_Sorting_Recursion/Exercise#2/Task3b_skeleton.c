
#include <SDL2/SDL.h>
#include <stdio.h>

SDL_Window *win;
SDL_Renderer *ren;

void drawsquare(double x, double y, double l) {
	SDL_Rect rect = { x, y, l, l }; // x, y, width, height
	SDL_RenderFillRect(ren, &rect);
	SDL_RenderDrawRect(ren, &rect);
	SDL_RenderPresent(ren);
}

/********Add Recursive TSquareFractal function here*******/
 void TSquareFractal(double x, double y, double l, int i){
     if (i == 0){
         return;
     }
    
     drawsquare(x,y,l);
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

	int main(int argc, char *argv[]) {
	if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
		printf("SDL could not initialize");
	}

    
    int iters = 4;
	SDL_CreateWindowAndRenderer(1000, 1000, 0, &win, &ren);
	SDL_SetRenderDrawColor(ren, 255, 255, 255, 255);
	SDL_RenderClear(ren);

	SDL_SetRenderDrawColor(ren, 0, 0, 0, 255);
	
/********Call Recursive TSquareFractal function here*******/	
    TSquareFractal(0,0,1000,iters);
	SDL_Event e;
	do { SDL_PollEvent(&e); } while (e.type != SDL_MOUSEBUTTONDOWN);
}

