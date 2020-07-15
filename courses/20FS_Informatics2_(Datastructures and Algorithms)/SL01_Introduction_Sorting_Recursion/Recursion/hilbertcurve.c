#include <stdio.h>
#include <SDL2/SDL.h>

SDL_Window *win;
SDL_Renderer *ren;

float x,y,u;

// u is the line lengths

void drawLine(float dx, float dy){
    SDL_RenderDrawLine(ren, x, y, x+dx, y+dx);
    x = x + dx;
    y = y + dy;
    SDL_Delay(5);
    SDL_RenderPresent(ren);
}

void HilbertA(int); void HilbertB(int); void HilbertC(int); void HilbertD(int);

void HilbertA(int d){
    if (d > 0){
        // A = B <- A (Down) A -> C
        HilbertB(d-1); drawLine(-u, 0);
        HilbertA(d-1); drawLine(0, -u);
        HilbertA(d-1); drawLine(u, 0);
        HilbertC(d-1);
    }   
}

void HilbertB(int d){
    if (d > 0){
        // B = A (Down) B <- B (up) D
        HilbertA(d-1); drawLine(0,u);
        HilbertB(d-1); drawLine(-u, 0);
        HilbertB(d-1); drawLine(0,-u);
        HilbertD(d-1);
    }
}

void HilbertC(int d){
 if (d > 0){
        // C = D (up) C -> C (down) A
        HilbertA(d-1); drawLine(0,-u);
        HilbertB(d-1); drawLine(u, 0);
        HilbertB(d-1); drawLine(0,u);
        HilbertD(d-1);
    }
}

void HilbertD(int d){
 if (d > 0){
        // D = C -> d (up) D <- B
        HilbertC(d-1); drawLine(0,u);
        HilbertD(d-1); drawLine(-u, 0);
        HilbertD(d-1); drawLine(0,-u);
        HilbertB(d-1);
    }
}

int main(int argc, char** argv){
    int d;
    sscanf(argv[1], "%d", &d);

    SDL_CreateWindowAndRenderer(400, 400, 0, &win, &ren);
    SDL_SetRenderDrawColor(ren, 255, 255, 255, 0);
    x = 395;
    y = 5;
    u = 390 / (pow(2,d)-1);
    HilbertA(d);

    SDL_Event e;
    do { SDL_PollEvent(&e); } while (e.type != SDL_QUIT);
    return 0;
}
