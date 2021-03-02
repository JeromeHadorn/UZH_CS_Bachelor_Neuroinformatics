function [x] = MonomialMethod(nodes, y)
% x         coefficents
% nodes     x values
% y         evalued nodes

N = length(nodes)
A = ones(N, N)

for i=1:length(nodes)
    for j=1:length(nodes)
        A(i,j) = nodes(i)^(j-1)
    end  
end

x = A \ y'
end

