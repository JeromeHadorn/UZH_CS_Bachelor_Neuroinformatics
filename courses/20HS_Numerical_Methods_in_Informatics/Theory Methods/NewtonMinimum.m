x0 = [-4;0;];
tol = 10^-5;
itMax = 100;
x0 = -2;
[x, y, iter] = NewtonMin(@fun, @jacobian, x0, tol, itMax)

function [x, y, iter] = NewtonMin(Ffun, JacobianFun, x0, tol, itMax)
    iter = 0;
    err = tol + 1;
    x = x0; % first guess

    while (err >= tol & iter < itMax)
        J = JacobianFun(x);
        F = Ffun(x);
        delta = -J \ F;
        x = x + delta;
        err = norm(delta)
        iter = iter + 1;
    end
    y = norm(Ffun(x));
end


function F = fun(x) % aka gradient
    F(1,1) = x(1)/5 + 2 * cos(x(1));
end

function J = jacobian(x) % aka hession
    J(1,1) = (1/5 - 2 *sin(x(1)));
end


