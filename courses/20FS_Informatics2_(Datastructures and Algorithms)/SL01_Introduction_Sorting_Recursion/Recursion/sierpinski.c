#include <stdio.h>
#include <SDL2/SDL.h>

SDL_Window * win;
SDL_Renderer *ren;

int x,y,h,d;


void triangle(int x1, int x2,  int y1, int y2, int z1, int z2){ 
    SDL_RenderDrawLine(ren, x1, x2, y1, y2);
    SDL_RenderDrawLine(ren, y1, y2, z1, z2);
    SDL_RenderDrawLine(ren, z1, z2, x1, x2);
    SDL_Delay(5);
    SDL_RenderPresent(ren);
}

void sierpinski(int x, int y, int h, int d){
    if (d > 0){
        
        // Draw Triangle with following three points
        triangle(x-(h/2), y, x + (h/2), y, x, y + h);

            sierpinski(x-(h/2), y + (h/2), h/2, d-1);
            sierpinski(x+(h/2), y + (h/2), h/2, d-1);
            sierpinski(x,y-h, h/2, d-1);
    }
}



int main(){

    SDL_CreateWindowAndRenderer(400, 400, 0, &win, &ren);
    SDL_SetRenderDrawColor(ren, 255, 255, 255, 0);
    x=200; y=200;h=200;d=2;
    sierpinski(x,y,h,d);
    SDL_Event e;
    do { SDL_PollEvent(&e); } while (e.type != SDL_QUIT);
    return 0;
}
