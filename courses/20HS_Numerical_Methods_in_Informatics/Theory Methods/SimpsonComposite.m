function [AproxIntegral] = SimpsonComposite(fun,a,b,M)
    %% Input
    %   fun     function in vector form .* etc.
    %   a       start interval
    %   b       end interval
    %   M       number of subintervals to create
    %% Output
    %   AproxIntegral - Area of summed subintervals
    %% Code
    h = (b-a)/M % length of an inteval

    x1 = a;
    xM = b;

    EquiSpacedNodes = linspace(x1 ,xM, M);
    EquiSpacedMidPoints = linspace(x1+h/2,xM-h/2,M-1);
    
    funAtNodes = fun(EquiSpacedNodes)
    funAtMidpoints = fun(EquiSpacedMidPoints)
    
    simpsonSum = 0;
    for i=1:M-1
        simpsonSum = simpsonSum + funAtNodes(i) + 4*funAtMidpoints(i) + funAtNodes(i+1);    
    end
    
    AproxIntegral = h/6 *  simpsonSum;
end


function [AproxIntegral] = comp_simpson(fun,a,b,M)
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
       c1 = fun(0.5*(xx(k)+xx(k+1)));
       
       II = II + (h/6)*(a1+b1+4*c1)
   end
   AproxIntegral = II;
end


