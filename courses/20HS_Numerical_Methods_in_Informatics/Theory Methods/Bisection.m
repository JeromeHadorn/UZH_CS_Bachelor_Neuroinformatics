function [x,it] = Bisection(fun, x0, x1, eps)
    % Input:
    %      fun (function handle): the function to find the root for
    %      x0  (float):           the lower bound of the interval
    %      x1  (float):           the upper bound of the interval
    %      eps (float):           the given tolerance
    Nmax = 5000;
    
    % Initialising the iteration number and setting
    % an error bigger than eps to enter in the loop
    it  = 0;
    err = eps+1;
    
    % Initialising the considered interval bounds
    a = x0;
    b = x1;
    
    % Defining the iteration loop that is computing the bisection
    while ((err>eps)&&(it<Nmax))
        % Evaluate the midpoint of the interval
        mid=(a+b)*0.5;
        % Check which part of the interval to select
        if (fun(a)*fun(mid)<0)
             b=mid;
        else
            a=mid;              
        end
        % Computing the error (the stopping criterion)
        % and incrementing the number of iterations
        err = 0.5*abs(b-a);
        it  = it+1;
    end
    
    % Informing the user of the function output
    if ((err>eps) || (it>Nmax))
        % Case where the function failed to find the zero before the
        % allowed number of iterations
        error(sprintf("After %d iterations, no root has been found with the desired accuracy.", it))
    else
        % Informing the user
        fprintf("The number of iterations required to achieve the tolerance %f is %d\n", eps, it);
        % Estimate the zero as the mid point of the found interval
        x = (a+b)*0.5;
        fprintf("The root is located within the interval [%d, %d]\n", a, b);
    end
end
