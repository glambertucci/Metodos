function [t y]=heun(f,y0,t0,tf,n)
h=(tf-t0)/n;
t=linspace(t0,tf,n+1);
y(1,:)=y0;
for i=1:n
k1(i,:)=f(t(i),y(i,:));
k2(i,:)=f(t(i)+h,y(i,:)+k1(i,:));
y(i+1,:)=y(i,:)+(h/2)*(k1(i,:)+k2(i,:));
end
end