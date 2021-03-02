function [x] = BackwardSubstitution(U,b)
    %% Input
    %   U   Upper triangular Matrix - is nonsingular - no zeros in diagonal
    %   b   Result Vector
    %% Output
    %   x   Result for U*x = b
    %% Code
    n = size(b,2)
    x = zeros(1,n)

    for i=n:-1:1
            xi= 1/U(i,i) .* (b(i)- sum( U(i,i+1:end) .*x (i+1:end) ) );
            x(i)=xi;
    end
    x=x';
end
