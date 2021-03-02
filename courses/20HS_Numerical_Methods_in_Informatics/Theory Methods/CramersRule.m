function [x] = CramersRule(A,b)
    %% Input
    %   A   nonsingular Matrix A
    %   b   result vector b
    %%Output
    %   x   Solution to A*x = b
    %% Method
    [rownum,colnum]=size(A)
    x = []
    detA = det(A)
    for i=1:colnum
        copyA = A;
        copyA(:,i) = b
        x_i = det(copyA)/detA
        x = [x,x_i]
    end
end

