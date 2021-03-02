function [phi] = LagranCharPoly(nodes, x)
    %% Input Variables
    % nodes         vector of nodes
    % x             vector x
    %% Output Variables
    % phi           Matrix X x Nodes

    % Init Matrix Filled with Ones
    phi = ones(length(x), length(nodes));
    % Lagrange Polynomial Builder
    for i = 1:length(x) % for each row in phi
        for k=1:length(nodes) % for each column comp. in row i
            for j=1:length(nodes)
                if j ~= k
                    phi(i,k) = phi(i,k) * ((x(i)- nodes(j)) / (nodes(k) - nodes(j)));
                end
            end
        end
    end
end