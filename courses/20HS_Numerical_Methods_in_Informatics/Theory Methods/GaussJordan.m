function x = GaussJordan (A,b)
    % Solve the problem Ax=b using Gauss-Jordan method
    % We suppose that no pivoting is required
    % INPUT :   A:   Coefficient matrix
    %           b:   Right-hand term
    %
    % OUPUT :   x:   Solution

    % Error message if necessary
    [n,m]=size(A);
    b=b(:); %Column vector

    % Concatenation
    A=[A b];

    % Reduction
    for j=1:n %Go accross columns (except last: it is b) : each pivot
       for i=1:n %Accross rows: goal: eliminate the rest of the column
           if i~=j %Reduction on all rows except itself
               factor=A(i,j)/A(j,j);
    %            A(i,:)=A(i,:)-A(j,:)*A(i,j)/A(j,j);
               for k=1:(n+1)
                   A(i,k)=A(i,k)-A(j,k)*factor;
               end
           end
       end
    end

    % Debug A

    % Init output
    x=0.*b;

    % Retrieve modified b
    b=A(:,end);


    % Final solving
    for i=1:n
        x(i)=b(i)/A(i,i);
    end
end


A=eye(3);b=(1:3)';
GaussJordan(A,b)
A\b
fprintf("\n")
