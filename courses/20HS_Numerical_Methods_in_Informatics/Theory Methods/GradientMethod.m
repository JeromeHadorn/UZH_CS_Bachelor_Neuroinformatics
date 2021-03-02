function [x] = GradientMethod(A,b,x0,tol,itMax)
    %% Input
    % A     square matrix no zeros in diag
    % b     Solution to Ax
    % x0    Start guess
    % tol   error tolerance
    % itMax max iteration
    %% Output - x Approximated result for Ax = b
    x = x0;
    r = b - A*x;
    rel_error = tol * 2; % norm(x - x0)/norm(x);
    it = 1;
    
    while(rel_error > tol & it < itMax)
        x_prev = x;
        
        s = A*r;
        alpha = ((r')*r) / ((r')*s)
        
        x = x + alpha*r;
        r = r - alpha*s; % calculating new residual
        rel_error = norm(x - x_prev)/norm(x); % error
        it = it + 1;
    end
end

