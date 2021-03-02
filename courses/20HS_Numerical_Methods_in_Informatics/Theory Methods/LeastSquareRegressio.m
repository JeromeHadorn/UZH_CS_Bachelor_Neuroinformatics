xx = 1
yy = 2

%% Least square regressions
ls1= polyfit(xx,yy,1); %Coefs
ls2= polyfit(xx,yy,2);
ls4= polyfit(xx,yy,4);

y1=polyval(ls1, xx); %y values (polynomial evaluation)
y2=polyval(ls2, xx);
y4=polyval(ls4, xx);

%% Maximum residual
max_er1=max((y1-yy).^2);
max_er2=max((y2-yy).^2);
max_er4=max((y4-yy).^2);

fprintf("Maximum square residual (weekly):\n")
fprintf("   Degree 1: %.2f\n",max_er1)
fprintf("   Degree 2: %.2f\n",max_er2)
fprintf("   Degree 4: %.2f\n",max_er4)
% Not very relevant