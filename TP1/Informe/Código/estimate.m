function he = estimate (S, rE)
[U,S,V] = DVS(S);
he = zeros(size(V,2),1);
for k=1:size(V,2)
  he= he+(U(:,k)'*rE*V(:,k))/S(k,k);
end