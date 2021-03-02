x0 = [-1;1;];
tol = 10^-5;
itMax = 100;
B0 = [-1.5,1.5;-3.5,-0.5]
[x, y, iter] = Broyden(@fun, B0, x0, tol, itMax)

function [x, y, k] = Broyden(Ffun, B0, x0, tol, itMax)
    err = tol + 1;
    B = B0
    B(:,:,1) = B0;
    x = x0
    x(:,:,1) = x0
    
    k = 1; % iterator
    while (err >= tol & k < itMax)
        
        F = Ffun(x(:,:,k));
        delta = -B(:,:,k) \ F;
        x(:,:,k+1) = x(:,:,k) + delta;
        
        F1 = Ffun(x(:,:,k+1));
        deltaF = F1 - F;
        
        B(:,:,k+1) = B(:,:,k) + (((deltaF-B(:,:,k)*delta)*delta')/((delta')*delta))
        
        err = norm(delta)
        k = k + 1;
    end
    y = norm(Ffun(x(:,:,k-1)));
end


function F = fun(x)
    F(1,1) = x(1)^2 + x(2)^2 -1;
    F(2,1) = x(1)^2 - 2*x(1)-x(2) + 1;
end


