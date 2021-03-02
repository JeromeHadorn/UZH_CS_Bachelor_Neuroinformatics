function [e] = GramSchmidt(A)
    %% Given the input we must find a set of orthonormal vectors spanning the same space
    %% Input - A is an array of column vectors
    %% Output - orthonormal vectors spanning the same space
    %%
    % Initiliazing Variables
    n = size(A,2);
    e = zeros(n);

    % Setting the first column vector
    u1 = A(:,1);
    e(:,1) = u1 / norm(u1);


    for j=2:n  % For each column
        u_j = A(:,j);

        % Calculating the Projetion
        projection = 0;
        for k=1:j-1
            e_k = A(:,k);
            projection = projection + dot(u_j,e_k) * e_k;
        end

        v = u_j - projection;
        e(:,j) = (v / norm(v))
    end
end



