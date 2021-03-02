function [xs] = fixed_point(func, a, b, n)
	% Function that performs the fixed point iteration method to find the zeros of a function f given the associated 
	% iteration function func.
	%   Args:
	%        func (function handle): the iteration function func (associated to the consired function f to find the zero for)
	%        a,b  (floats):          the bounds of the considered interval
	%        n    (integer):         the number of iterations to perform
	%   Returns
	%        xs   (float list):      the abscissa of the found zero of the function f
	%  Warning: the function does not tell you directly whether you converged or not
			
	% Creating a first guess and initialising the quantities 
	x0 = a+0.8*(b-a)   % Setting the guess to be at 80% of the considered interval far from a 
	xs=[x0];
	
	% Iterating a prescribed number of times
    % (for the sake of the examle we here consider a precise number of time step)
	for it = 1:n
		% Evaluating the value of the iterator function at the given point
		x1 = func(x0);
		% Updating the current value of the approximated zero
		x0 = x1;
		% Keeping track of the old values
		xs = [xs;x1];
	end
end