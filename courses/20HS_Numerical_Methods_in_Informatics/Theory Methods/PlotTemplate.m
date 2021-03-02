

%% Plot Section
x = linspace(1,100,100);
fun = @(x)  x.^2;

fig = figure()

plot(x,fun(x),"--r","DisplayName","Some Value")
xlabel("X")
ylabel("Y")
title("Title of maaa Plot")
legend("Some curve1")
%savefig("ma_fig.fig")
%close()