function [R] = Cholesky(A)
    %% Input - A (symmetric, positive definite
    %% Output - R upper triangular matrix such that R*R' = A
    %%
    n = size(A, 1); % Obtain number of rows or columns (quadratic!)
    R = zeros(n); % Upper triangular matrix
    
    R(1,1) = sqrt(A(1,1)) % Initialize first value
   
    for j=2:n
        for i=1:j-1
            sum1 = 0
            for k=1:i-1
                sum1 = sum1 + R(k,i)*R(k,j);
            end
            R(i,j)=(A(i,j)-sum1)/R(i,i);
        end
        sum2 = 0;
        for k=1:j-1 
            sum2 = sum2 + R(k,j)*R(k,j);
        end
        R(j,j)=sqrt(A(j,j)-sum2);
    end
end