function [lambda, xx, iter, lambdas, xxs] = powershift(A, alpha, tol, itMax, x0)
    % Powershift method to compute largest eigenvalue of a matrix A-alpha*I
    %% Initalisation
    n = size(A,1);
    B=A-eye(n)*alpha;
    err = 1e10;
    iter = 0;
    xx = x0;
    yy = xx/norm(xx,2);
    
    lambdas = zeros(1,itMax);
    xxs=zeros(n,itMax);
    
    
    while err>= tol && iter<itMax
        
        % Calculate the new eigenvector
        xx = B*yy;
        yy = xx/norm(xx,2);
        
        % Calculate the new eigenvalue
        lambda = yy'*(B*yy);
        
        % New iter and storage of the history
        iter = iter + 1;
        xxs(:,iter) = yy; % Normalised output for eigenvector estimation
        
        lambdas(iter) = lambda + alpha; % Don't forget the shift
        
        if iter>1
            err = abs(lambdas(iter) - lambdas(iter-1)) / abs(lambdas(iter) - alpha);
        end
    end
    
    % Just sending the truncated important data back
    lambda = lambda + alpha;
    lambdas = lambdas(1:iter);
    xxs = xxs(:,1:iter);
    xx = yy; % Final normalized xx
end