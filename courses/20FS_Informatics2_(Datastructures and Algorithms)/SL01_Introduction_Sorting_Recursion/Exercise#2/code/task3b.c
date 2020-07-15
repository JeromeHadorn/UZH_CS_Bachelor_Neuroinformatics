
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

void TSquareFractal(double x, double y, double length, int iter) {
   if(iter == 0) return;
    drawsquare(x,y,length);
    SDL_Delay(50);
    TSquareFractal(x-length/4,y-length/4,length/2,iter-1);  //Lower left Corner
    TSquareFractal(x-length/4,y+ (3.0/4.0)*length,length/2,iter-1);  //Upper left Corner
    TSquareFractal(x+(3.0/4.0)*length,y-length/4,length/2,iter-1);  //Lower Right Corner
    TSquareFractal(x+(3.0/4.0)*length,y+(3.0/4.0)*length,length/2,iter-1);  //Upper Right Corner

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
	TSquareFractal(300, 300, 400, iters);

	SDL_Event e;
	do { SDL_PollEvent(&e); } while (e.type != SDL_MOUSEBUTTONDOWN);
}

// Linux: gcc task3b.c -o task3b -lm -lSDL2; ./task3b