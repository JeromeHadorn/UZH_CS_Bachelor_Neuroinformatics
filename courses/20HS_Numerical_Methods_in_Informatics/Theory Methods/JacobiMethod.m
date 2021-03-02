function [x] = JacobiMethod(A,b,x0,tol,itMax)
    %% Input
    % A     square matrix no zeros in diag
    % b     Solution to Ax
    % x0    Start guess
    % tol   error tolerance
    % itMax max iteration
    %% Output - x Approximated result for Ax = b
    %%
    P = diag(diag(A)); % Building D
    x = x0;
    r = b - A*x;
    rel_error = tol * 2; % norm(x - x0)/norm(x);
    it = 1;
    
    while(rel_error > tol & it < itMax)
        x_prev = x;
        
        z = P\r; % Solve Dz = r
        
        x = x + z;
        r = b - A*x; % calculating new residual
        rel_error = norm(x - x_prev)/norm(x); % error
        it = it + 1;
    end
end

