%% Cleaning the environment
clear all;
close all;
clc;


%% Defining the problem of interest

% Defining the problem and the wished parameters for its resolution
u_ex = @(x,y) exp(x+y/2);         % Defining the exact solution of the problem
fun  = @(x,y) 1.25*exp(x+y/2);    % Investigated source function in the posson problem
uL   = @(x,y) exp(y/2);           % Boundary conditions: uLeft     for x=0
uR   = @(x,y) exp(1+y/2);         % Boundary conditions: uRight    for x=1
uB   = @(x,y) exp(x);             % Boundary conditions: uBottom   for y=0
uT   = @(x,y) exp(x+1/2);         % Boundary conditions: uTop      for y=1
a=0;b=1;c=0;d=1;                  % Investigating the solution in the unit square



%% Define the discretisation, generate the matrix and compare it with the matlab's construction

% Number of wished subintervals per dimension (uniform grid discretisation)
N = 20;                          

% Generating the grid discretisation
x = linspace(a,b,N+2);                        % Spacing vector for x direction
y = linspace(c,d,N+2);                        % Spacing vector for y direction
h = x(2)-x(1);                                % Computing the spacing
[xx,yy] = meshgrid(x(2:end-1),y(2:end-1));    % Creating the grid discretisation excluding the boundaries
[xxb,yyb] = meshgrid(x,y);    % Creating the grid discretisation excluding the boundaries

% Plotting the discretisation
fig = figure();
hold on
mesh(xx,yy,0*xx)                              % Plotting the mesh as a zero-wireframe solution
view(0,90)                                    % Projecting on a 2D visualisation
plot(xx,yy,"*r")                              % Plotting the nodes
plot([a,b,b,a,a],[c,c,d,d,c],"-k")            % Plotting the domain
hold off
axis([a-0.1, b+0.1, c-0.1, d+0.1])            % Adjusting the visualisation bounding box
title("Mesh in use for solving the problem")  % Customisations
xlabel("x"); ylabel("y")
legend("Mesh","Nodes")


% Constructing the vector b over the designated grid
xx = xx'; yy = yy';                                % Transpose so that  xx(i,j), yy(i,j) are coordinates of (i,j) point
bMatr = (h^2)*fun(xx,yy);                          % Applying the source term at each grid point
bMatr(1,:) = bMatr(1,:)+uL(xx(1,:),yy(1,:));       % Applying the left boundary condition
bMatr(:,1) = bMatr(:,1)+uB(xx(:,end),yy(:,end));   % Applying the bottom boundary condition
bMatr(N,:) = bMatr(N,:)+uR(xx(end,:),yy(end,:));   % Applying the right boundary condition
bMatr(:,N) = bMatr(:,N)+uT(xx(:,end),yy(:,end));   % Applying the top boundary condition

% Rearrange the components of bMatr in a vector shape
% b= [bMatr(:,1) bMatr(:,2) ... bMatr(:,N)]'; % -> so it is [b_11 b_12 ... b_1N ..  b_21 ...   b_NN]
b = reshape(bMatr,N*N,1);

% Construct the matrix A
%A = ConstructA(N);

% Compare it with the matrix retrieved from Matlab
A1 = gallery('poisson',N);

%fprintf("Matrices construction comparison, %f\n", max(max(abs(A-A1))));