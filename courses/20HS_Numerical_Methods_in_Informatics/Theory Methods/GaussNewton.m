
tol = 10^-5;
itMax = 100;
x0 = [0;0]; % initial guess
fun = @(x) [ x(1)-.4; x(2)-.8 ; x(1)^2+x(2)^2-1 ];
jacobian = @(x) [ 1,0 ; 0,1 ; 2*x(1),2*x(2) ];  % define Jacobian fp(x)
b = [ 0.0375; 0.0750;-0.0429;]


[x, y, iter] = GaussNewtonMethod(fun, jacobian, x0,b, tol, itMax)

function [x, y, iter] = GaussNewtonMethod(Ffun, JacobianFun, x0,b, tol, itMax)
    iter = 0;
    err = tol + 1;
    x = x0; % first guess

    while (err >= tol & iter < itMax)  
        J = JacobianFun(x)' * JacobianFun(x);
        F = JacobianFun(x)' * (b-Ffun(x));
        
        
        delta = J \ F;
        x = x + delta;
        
        err = norm(delta)
        iter = iter + 1;
    end
    y = norm(Ffun(x));
    
    %% Plot
    plot(x(1),x(2),'k*'); hold off %    mark solution point with '*'
    title('Solution of nonlinear least squares problem (*)')
end
