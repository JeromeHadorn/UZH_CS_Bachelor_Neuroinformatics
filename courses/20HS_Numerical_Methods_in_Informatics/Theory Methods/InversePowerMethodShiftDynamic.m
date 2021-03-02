function [eigenvector,eigenvalue] = InversePowerMethodShiftDynamic(A,x0,alpha, tol,itMax)
    %% Input
    %   A   -   a square matrix
    %   x   -   n initial vector
    %   alpha - value to find the closest eigenvalue to    
    %   tol -   error tolerance
    %   itMax - max Iterations
    %% Output
    %   eigenvector - dominant eigenvector
    %   eigenvalue  - dominant eigenvalue
    %%
    n = size(A,1);
    x = zeros(n,itMax)
    y = zeros(n,itMax)
    lambda = zeros(1,itMax); % Eigenvalues belonging to B
    lambdaAlpha = zeros(1,itMax); % Eigenvalues belonging to A
    

    x(:,1) = x0; % initial vector
    y(:,1) = x(:,1) / norm(x(:,1));
    lambdaAlpha(1) = (y(:,1)') * (A * y(:,1));

    
    k = 2; %Iterator
    while(k<itMax & norm(y(:,k)-y(:,k-1)) > tol)
        
        B = A - (lambdaAlpha(k-1) * eye(n));
        
        x(:,k) = B \ y(:,k-1);
        y(:,k) = x(:,k) / norm(x(:,k));
        
        lambda(k) = (y(:,k)') * x(:,k);
        lambdaAlpha(k) = 1 / (lambda(k)) + alpha;

        k = k+1;
    end
    
    eigenvector = y(:,k-1)
    eigenvalue = lambdaAlpha(k-1)
end

