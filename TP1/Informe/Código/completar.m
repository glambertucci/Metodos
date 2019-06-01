function [Ucompleta] = completar(U)
%completar U toma una matriz U de m*n y devuelve otra matriz de m*m
%ortonormal

[m,n] = size(U);
U = [U zeros(m, m-n)];
for i = 1:(m-n)
    vec = rand([m 1]);
    vecOrt = vec - sum(((vec'*U).*U),2); %ortogonalización de vec
    U(:,n+i) = vecOrt/norm(vecOrt); %normalización del vector
end
Ucompleta = U;
    
    
end

