function [L,U, P] = LUDecompositionPivot(A)
    % LU Decomp. with Partial Pivoting
    %% INPUT
    % A     nonsingular, quadratic Matrix A, with no zeros please
    %% OUTPUT
    % L     lower triangular matrix with multiplication factor and a
    % diagonal full of ones
    % U     upper triangular matrix with modified values from A
    % P     Identidy Matrix with shifted row information
    %%
    n = size(A, 1); % Obtain number of rows or columns (quadratic!)
    P = eye(n);
    U = zeros(n);
    % Default 1 as diagonal
    L = zeros(n); % Start L off as identity and populate the lower triangular half slowly

    for k = 1 : n
        % find the entry in the left column with the largest abs value (pivot)
        [~,r] = max(abs(A(k:end,k)));
        r = n-(n-k+1)+r;    

        A([k r],:) = A([r k],:);
        P([k r],:) = P([r k],:);
        L([k r],:) = L([r k],:);
        
          % from the pivot down divide by the pivot
        L(k:n,k) = A(k:n,k) / A(k,k);

        U(k,1:n) = A(k,1:n);
        A(k+1:n,1:n) = A(k+1:n,1:n) - L(k+1:n,k)*A(k,1:n);
    end
    U = A;
end