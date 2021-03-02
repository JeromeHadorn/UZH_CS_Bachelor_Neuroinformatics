x = rand(1, 100);
x = 100*x./sum(x);
% Generate a matrix whose eigenvalues are the elements of x
A = gallery('randcorr', x);

largest = eigs(A, 1, 'lm')