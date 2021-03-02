function [Q,R] = QRFactorization(A)
    %% Given the input we must find a set of orthonormal vectors * a projection = A; Q*R = A
    %% Input - A is an array of column vectors
    %% Output - Q - being the Grahm Schmidt orthogonal vectors, R projection of A on Q
    %%
    % Initiliazing Variables
    [n, m] = size(A)
    Q = zeros(n,m)
    R = zeros(n,n)
    
    for j=1:n
        q_j = A(:,j);
        for i =1:j-1
            R(i,j) = Q(:,i)' * A(:,j)
            q_j = q_j - R(i,j) * Q(:,i); % subtracting the projection
        end   % v is now perpendicular to all q1  - qj-1
        R(j,j) = norm(q_j)
        Q(:,j) = q_j / R(j,j);  % Normalizing v to be the next unit vector
    end
end
