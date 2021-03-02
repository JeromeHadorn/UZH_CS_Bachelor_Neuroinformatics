function [phi] = BarycentricFormula(nodesX, nodesY, x)
    %% Input Variables
    % nodes         vector of nodes
    % x             vector x
    %% Output Variables
    % phi           Matrix X x Nodes

    % Init Matrix Filled with Ones
    phi = ones(length(x), length(nodesX));
    % Lagrange Polynomial Builder
    for i = 1:length(x) % for each row in phi
        for k=1:length(nodesX) % for each column comp. in row i
%             for j=1:length(nodesX)
%                 if j ~= k
%                     phi(i,k) = phi(i,k) * ((x(i)- nodesX(j)) / (nodesX(k) - nodesX(j)));
%                 end
%             end


                % Calculate weights
                weights = 
                % phi(i,k)
                phi(i,k) = weights
                
                
        end
    end

    evaluatedPoints = sum(phi. * nodesY, 2); % sums by row keeping it a column vector
    
    plot(x, evaluatedPoints);
end