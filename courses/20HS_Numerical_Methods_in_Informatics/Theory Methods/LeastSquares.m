function [coeff] = leastSquares (xxs, yys, m)
    %% Input
    %   xxs     x value of data nodes
    %   yys     y value of data nodes
    %   m       degree of polynomial approximating data
    %% Output
    %   coeff [a0, a1, ..., an]

    yValues = yys'; % make it a column

    %% Construct Matrix A
    % [1, x_1^1, x_1^2;
    %  1, x_2^1, x_2^2 ]
    a = [];
    for row=1:length(xxs)
        currentRow = [];
        currentM = m;
        for i=1:m+1
            currentRow = [currentRow, xxs(row)^currentM];
            currentM = currentM - 1;
        end
        a = [a; currentRow];
    end
    coeff = a\yValues;
end