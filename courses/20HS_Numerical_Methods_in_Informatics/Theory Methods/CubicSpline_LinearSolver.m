function [coeff] = CubicSpline(nodes,yys)
    % Method to perform Natural Spline Coeficents Creation
    % Arguments:
    %   nodes - n+1 number of nodes
    %   yys - n+1 values for corresponding to nodes
    % Outputs:
    %   coeff - coefficent matrix of size n * 4
    n=length(nodes);
    a=zeros(n-1,1);
    b=zeros(n-1,1);
    AA=zeros(n-2,n-2); % intermediate step matrix for c vector
    d=zeros(n-1,1);
    %% Step Size Creation - Computing the horizontal gap vector
    h = nodes(2:end)-nodes(1:end-1);
    %% Calculate a
    for i=1:n-1
        a(i)=yys(i);
    end
    %% Setting up AA Matrix to get c
    % Assigning Default Values
    AA(1,1)=2/3 *h(1)^2 + h(2)-1/3*h(2)^2;
    AA(1,2)=1/3*h(2)^2;
    % Populating n-2 row entries
    AA(n-2, n-3) = h(n-3)-2/3*h(n-3)^2;
    AA(n-2,n-2) = 2/3*h(n-3)^2 + h(n-2)-1/3*h(n-2)^2;
    % Assinging Values based on Formulas
    for i=2:n-3
        AA(i,i-1)= h(i-1)-2/3*h(i-1)^2;
        AA(i,i)= 2/3*h(i-1)^2 + h(i)-1/3*h(i)^2;
        AA(i,i+1)= 1/3*h(i)^2;
    end
    for i=2:length(yys)-1
        y(i-1)=(yys(i+1)-yys(i))/h(i)-(yys(i)-yys(i-1))/h(i-1);
    end

    c = AA\y';
    c = [0;c]; %% appending empty 0 as first entry
    %% Calculate d
    for i=1:n-2
        d(i)=1/3*(c(i+1)-c(i));
    end
    d(n-1)=1/3*(-c(n-1));
    %% Calculate b
    for i=1:n-1
        b(i)=(yys(i+1)-yys(i))/h(i) - c(i)*h(i)-d(i)*h(i)^2;
    end
    %% Return coefficent
    coeff=[d c b a];
end