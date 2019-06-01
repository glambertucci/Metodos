function [U, S, V] = DVS (A)
  
m = size(A,1); %número de filas de A
n = size(A,2); %número de columnas de A
Uprov = zeros(m,m);
V = zeros(n,n);
S = zeros(m,n);
B=A'*A;
[V,sigma] = eig(B);
sigma2 = sort(diag(sigma),'descend'); %se ordenan los autovalores
V=fliplr(V); %se ordenan los autovectores
Sig=sqrt(sigma2);
for k = 1:size(Sig)
    S(k,k)=Sig(k);
end
for k=1:n
    Uprov(:,k)=(A * V(:,k))/Sig(k);
end

if size(Uprov,2) < m
    U = completar(Uprov);
else
    U = Uprov;
end
