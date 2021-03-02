function [x_space, y_space] = PiecewiseLinearInterpolation (nodesX, nodesY)
    %% Input
    % nodesX = [3.0, 4.5, 7.0, 9.0]     Datapoints X
    % nodesY = [2.5, 1.0, 2.5, 0.5]     Datapoints Y
    %%

    x_space = [] % We create for each interval x values to be evaluated
    y_space = []

    for i = 1:length(nodesX)-1
        x = linspace(nodesX(i),nodesX(i+1),100)
        x_space = [x_space, x]
        y = nodesY(i) + (nodesY(i+1)-nodesY(i))/(nodesX(i+1)-nodesX(i)) * (x - nodesX(i)) % This is the slope formula
        y_space = [y_space, y]
    end


    plot(nodesX,nodesY,'bo',x_space,y_space,'r-')
    title 'Linear Piecewise Polynomial Interpolation'
    xlabel X
    ylabel Y
end