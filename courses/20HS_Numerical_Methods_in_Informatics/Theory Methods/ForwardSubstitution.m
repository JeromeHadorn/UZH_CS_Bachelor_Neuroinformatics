function [x] = ForwardSubstitution(L,b)
    %% Input
    %   L   Lower triangular Matrix - is nonsingular - no zeros in diagonal
    %   b   Result Vector
    %% Output
    %   x   Result for L*x = b
    %% Code
    n = size(b,2)
    x = zeros(1,n)

    for i=1:n
            xi= 1/L(i,i) .* (b(i)- sum( L(i,1:i-1) .*x (1:i-1) ) );
            x(i)=xi;
    end
    x=x';
end
