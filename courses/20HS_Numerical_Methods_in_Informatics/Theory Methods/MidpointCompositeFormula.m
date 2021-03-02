function [AproxIntegral] = MidpointCompositeFormula(fun,a,b,M)
    %% Input
    %   fun     function in vector form .* etc.
    %   a       start interval
    %   b       end interval
    %   M       number of subintervals to create
    %% Output
    %   AproxIntegral - Area of summed subintervals
    %% Code
    h = (b-a)/M % length of an inteval

    xMidpoint1 = a + h/2;
    xMidpointM = b - h/2;

    EquiSpacedNodes = linspace(xMidpoint1, xMidpointM, M);
    funEvaluatedAtNods = fun(EquiSpacedNodes);
    AproxIntegral =  sum(funEvaluatedAtNodes) * h;
end