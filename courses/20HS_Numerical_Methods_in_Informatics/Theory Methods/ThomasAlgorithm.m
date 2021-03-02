function [L,U,x] = ThomasAlgorithm(A,b)
    %% Input:    A  quadratic tridiagonal 
    %% Output:
    % L         lower matrix with one diagonal + 1 subdiag
    % U         upper matrix with main diag + upper diag of A
    % x         solution to the systems
    %%
    n=size(A,1);
    L = eye(n);
    U = zeros(n);
    
    U = U + triu(A,1) % Populate upper diag of U

    U(1,1) = A(1,1) % Default the first value
    for i=2:n
        L(i,i-1) = A(i,i-1) / U(i-1,i-1)
        U(i,i) = A(i-1,i-1) - L(i,i-1) * U(i-1,i)
    end
    
    y = L\b'
    x = U\y
end

