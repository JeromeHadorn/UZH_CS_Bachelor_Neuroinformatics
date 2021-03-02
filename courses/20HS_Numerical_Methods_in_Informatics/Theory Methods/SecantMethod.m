function [x, r, it, xxs] = NewtonMeth(fun, guess_1, guess_2, itMax, eps)
    %% INPUT:
    % fun           function handle,
    % guess_1       first guess
    % guess_2        second guess
    % itMax         number of maximum iterations
    % eps           prescribed convergence tolerance Îµ
    %% OUTPUT: 
    % x             approximate result,
    % r             residual at the last iteration,
    % it            number of perfomred iterations,
    % eps           vector containing all computed x^(k)
    %% Initalize Variables
    x(1) = guess_1; % First approximate result
    x(2) = guess_2; % Second approximate result
    r = abs(fun(x)); % First Residual
    it = 2; % Starting the Iterator at 2
    err = 1 + eps;  % giving a default error value bigger than eps
 
    %% Secant Method
    while(err > eps && it < itMax)% Condition: err must be bigger than eps and maxIteration isn't reached yet
        it = it + 1; % Increase iterator
        % Approximate x with the Secant instead of derivative
        x(it) = x(it-1) - (f(x(it-1)))*((x(it-1) - x(it-2))/(f(x(it-1)) - f(x(it-2))));
        err = abs(x(end) - x(end-1)); % Calculate relative error - absolue difference
        r = abs(fun(x_1)); % Calculate new residual
    end
end