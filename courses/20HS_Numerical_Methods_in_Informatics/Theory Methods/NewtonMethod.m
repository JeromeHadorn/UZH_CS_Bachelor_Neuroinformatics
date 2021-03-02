function [x, r, it, xxs] = NewtonMeth(fun, dfun, x0, itMax, eps)
    %% INPUT:
    % fun       function handle,
    % dfun      derivative function handle,
    % x0        inital value,
    % itMax     number of maximum iterations
    % eps       prescribed convergence tolerance Îµ
    %% OUTPUT: 
    % x         approximate result,
    % r         residual at the last iteration,
    % it        number of perfomred iterations,
    % eps       vector containing all computed x^(k)
    %% Initalize Variables
    x = x0; % First approximate result
    r = abs(fun(x)); % First Residual
    it = 0; % Starting the Iterator
    xxs = [x0]; % Initalizing xxs with the first guess
    err = 1 + eps;  % giving a default error value bigger than eps
 
    %% Newton Method
    % Condition: err must be bigger than eps and maxIteration isn't reached yet
    while(err > eps && it < itMax)
        it = it + 1; % Increase iterator
        x = x - (fun(x)/dfun(x)); % Approximate x
        xxs = [xxs, x]; % Append approximated value to xxs
        err = abs(xxs(end) - xxs(end-1)); % Calculate absolute error difference
        r = abs(fun(x)); % Calculate new residual
    end
end
