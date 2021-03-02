function [A]=ConstructPoissonMatrix(N)
    % Function constructing the matix associated to the posson problem
    %
    % Input:
    %      N: the size of the considered problem
    %
    % Output:
    %     A: the matrix A
    %

    % Creating the diagonal
    A = 4*eye(N^2);
        
    % Creating the upper and lower diagonals
    D1=-diag([repmat([ones(1,N-1),0],1,N-1),ones(1,N-1)],-1);
    D2=-diag([repmat([ones(1,N-1),0],1,N-1),ones(1,N-1)],+1);

    % Creating the very upper and very lower diagonal
    D3=-diag(ones(N^2-N,1),-N);
    D4=-diag(ones(N^2-N,1), N);
    
    % Concatenating
    A = A+D1+D2+D3+D4;
end