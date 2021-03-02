function [eigenvector,eigenvalue] = InversePowerMethod(A,x0,tol,itMax)
    %% Input
    %   A   -   a square matrix
    %   x   -   n initial vector
    %   tol -   error tolerance
    %   itMax - max Iterations
    %% Output
    %   eigenvector - dominant eigenvector
    %   eigenvalue  - dominant eigenvalue
    %%
    n = size(A,1);
    x = zeros(n,itMax)
    y = zeros(n,itMax)
    lambda = zeros(1,itMax);


    eigenvector = zeros(1,n)
    eigenvalue = 0

    x(:,1) = x0; % initial vecotr
    y(:,1) = x(:,1) / norm(x(:,1));


    k = 2; %Iterator
    while(k<itMax & norm(y(:,k)-y(:,k-1)) > tol)
        x(:,k) = A \ y(:,k-1);
        y(:,k) = x(:,k) / norm(x(:,k));
        lambda(k) = (y(:,k)') * x(:,k);

        k = k+1;
    end
    eigenvector = y(:,k-1)
    eigenvalue = 1/lambda(k-1)
end

