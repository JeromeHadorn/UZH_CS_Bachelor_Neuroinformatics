
tol = 10^-5;
itMax = 100;
x0 = [0;0]; % initial guess
fun = @(x) [ x(1)-.4; x(2)-.8 ; x(1)^2+x(2)^2-1 ];
jacobian = @(x) [ 1,0 ; 0,1 ; 2*x(1),2*x(2) ];  % define Jacobian fp(x)

[x, y, iter] = NonLinearLeastSquaresMethod(fun, jacobian, x0, tol, itMax)

function [x, y, iter] = NonLinearLeastSquaresMethod(Ffun, JacobianFun, x0, tol, itMax)
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
    
    %% Plot
    plot(x(1),x(2),'k*'); hold off %    mark solution point with '*'
    title('Solution of nonlinear least squares problem (*)')
end
