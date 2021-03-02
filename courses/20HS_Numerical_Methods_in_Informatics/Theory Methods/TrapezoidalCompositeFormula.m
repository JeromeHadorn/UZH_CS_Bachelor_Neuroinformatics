function [AproxIntegral] = TrapezoidalCompositeFormula(fun,a,b,M)
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

    EquiSpacedNodes = linspace(xMidpoint1 + h, xMidpointM - h, M-2); % We want interval without x1 and xM
    funEvaluatedAtNodes = fun(EquiSpacedNodes);
    
    AproxIntegral = h/2 * (fun(xMidpoint1) + 2 * sum(funEvaluatedAtNodes) + fun(xMidpointM)); 
end


function [AproxIntegral] = comp_trap(fun,a,b,M)
    %% Input
    %   fun     function in vector form .* etc.
    %   a       start interval
    %   b       end interval
    %   M       number of subintervals to create
    %% Output
    %   AproxIntegral - Area of summed subintervals
    %% Code
   xx = linspace(a,b,M+1);
   h = xx(2) - xx(1);
   
   II = 0
   
   
   for k=1:M
       a1 = fun(xx(k));
       b1 = fun(xx(k+1));
       
       II = II + (h/2)*(a1+b1)
   end
   AproxIntegral = II;
end





