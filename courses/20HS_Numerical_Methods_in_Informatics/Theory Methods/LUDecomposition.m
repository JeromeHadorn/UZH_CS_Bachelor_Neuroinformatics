function [L,U] = LUDecomposition(A)
    %% INPUT
    % A     nonsingular, quadratic Matrix A, with no zeros please
    %% OUTPUT
    % L     lower triangular matrix with multiplication factor and a
    % diagonal full of ones
    % U     upper triangular matrix with modified values from A
    %%
    n = size(A, 1); % Obtain number of rows or columns (quadratic!)

    % Default 1 as diagonal
    L = eye(n); % Start L off as identity and populate the lower triangular half slowly

    for k = 1 : n
        % For each row k, access columns from k+1 to the end and divide by
        % the diagonal coefficient at A(k ,k)
        L(k + 1 : n, k) = A(k + 1 : n, k) / A(k, k);

        % For each row k+1 to the end, perform Gaussian elimination
        % In the end, A will contain U
        for j = k + 1 : n
            A(j, :) = A(j, :) - L(j, k) * A(k, :);
        end
    end
    U = A;
end