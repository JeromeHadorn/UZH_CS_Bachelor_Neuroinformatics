% Defining the spline nodes
nodes = [0.25, 1.7057;
         0.75, 2.7449;
         1.3,  2.5580;
         1.7,  3.0326;
         1.9,  7.8285];

% Definition of the testing vector (where the path will be rebuilt)
x0 = 0.25; xn = 1.9;
xtest = linspace(x0, xn, 100);

%% Interpolating the quadratic spline
coeff = QuadraticSpline_Hand(nodes);% Retrieving the coefficients of the quadratic spline
ytestmat = Interpolating_Hand(nodes, xtest); % Retrieving the interpolating path

%% Plotting the reconstructed path and the sticks
fig = figure();
hold on 
plot(ytestmat(:,1), ytestmat(:,2), "--r")
plot(nodes(:,1), nodes(:,2), "or")
hold off
legend("Reconstructed path", "Nodes")
title("Path plot")
xlabel("x")
ylabel("y")

function [interppoints] = Interpolating_Hand(xx, xtest)
    % Initialising the interpolated vector
    ytest = [];
    xtt   = [];
    % Getting the interpolation coefficients from the nodes
    coeff = QuadraticSpline_Hand(xx);
    % Evaluate the points values depending on in which interval they lie
    for inter = 1:(length(xx)-1)
            % Retrieving the points living in the interval inter-1
            index = find((xx(inter+1)>=xtest) .* (xx(inter)<=xtest)); % we need this to know which row of the coefficent to use
            if ~isempty(index)
                % Tabulating the values
                xtemp = xtest(index)-xx(inter);
                % Constructing the determination matrix and retrieving the interpolated values
                A = [ ones(1, length(index)); xtemp; xtemp.^2];
                values = coeff(inter,:)*A;
                % Reconstructing the values within this interval
                ytest = [ytest, values];
                xtt   = [xtt, xtest(index)];
            end
    end
    % Returning the interpolated xy valyes
    interppoints = [xtt; ytest]';
end

function [coeff] = QuadraticSpline_Hand(nodes)
    % Function computing the coefficients of the quadratic spline in
    % the form si(x) = ai+bi(x-xi)+ci(x-xi)^2
    % Input:    (nx2 floats):  the nodes (abscissa and values) to be used to build the quadratic interpolation
    % Output:   (n x 3 floats):  the matrix containing the coefficents [c0 b0 a0]  associated to each node on a row
    n = length(nodes); % Retrieving the number of given nodes
    h = nodes(2:end,1)-nodes(1:end-1,1); % Computing the horizontal gap vector | x_i+1 - x_i
    a = nodes(1:end-1,2); %% Computing the coefficients ai | a_i = y_i
    %% Computing the coefficients  bi and ci
    c = zeros(n-1,1); % we already get c_0 = 0 here
    for k = 2:(n-1)
        c(k) = (1./h(k)).*((nodes(k+1,2)-nodes(k,2))./h(k)-(nodes(k,2)-nodes(k-1,2))./h(k-1)-c(k-1).*h(k-1));
    end
    b = (nodes(2:end,2)-nodes(1:end-1,2)) ./ h - c.*h; % Computing b knowing c
    coeff = [a'; b'; c']'; %% Concatenating the coefficients in  the matrix coeff
end