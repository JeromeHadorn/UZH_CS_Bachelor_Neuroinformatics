tol = 0.001;
x0 = -2;
fun = @(x)  2*sin(x)+(x^2)/10;
dfun = @(x) 2*cos(x) + x/5

itMax = 1000;
[x, y, iter] = GradientDescent(fun, dfun, x0, tol, itMax)



function [x, y, iter] = GradientDescent(Ffun, grad, x0, tol, itMax)
    iter = 0;
    err = tol + 1;
    x = x0; % first guess
    stepsize = 0.01;
    while (err >= tol & iter < itMax)
        x_prev = x
        x = x - stepsize*grad(x);
        err = abs(norm(x_prev-x,2));
        iter = iter + 1;
    end
    y = norm(Ffun(x));
end




