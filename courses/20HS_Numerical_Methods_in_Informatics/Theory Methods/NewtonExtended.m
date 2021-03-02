x0 = [-1;1;];
tol = 10^-5;
itMax = 100;
[x, y, iter] = NewtonMethodExtendedx(@fun, @jacobian, x0, tol, itMax)

function [x, y, iter] = NewtonMethodExtended(Ffun, JacobianFun, x0, tol, itMax)
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


function F = fun(x)
    F(1,1) = x(1)^2 + x(2)^2 -1;
    F(2,1) = x(1)^2 - 2*x(1)-x(2) + 1;
end

function J = jacobian(x)
    J(1,1) = 2*x(1);
    J(1,2) = 2*x(2);
    J(2,1) = 2*x(1) -2;
    J(2,2) = -1;
end


