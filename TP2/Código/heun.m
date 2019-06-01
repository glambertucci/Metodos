function [t x]=heun(f,x0,t0,tf,n,par)
	h=(tf-t0)/n;
	t=linspace(t0,tf,n+1);
	x(1,:)=x0;
	for i=1:n
		k1(i,:)=f(t(i),y(i,:),par);
		k2(i,:)=f(t(i)+h,y(i,:)+k1(i,:),par);
		x(i+1,:)=x(i,:)+(h/2)*(k1(i,:)+k2(i,:));
	end
end

function [t,x] = miode(f,x0,t0,tf,dtmax,tol,par)
	n = ceil((tf-t0)/dtmax);
	error=10 %Para que entre al while
	while(error>tol)
		[t1,x1]=heun(f,x0,t0,tf,n,par);
		[t2,x2]=heun(f,x0,t0,tf,2n,par);
		error = abs(x1(end,:)-x2(end,:));
		n = n+1;
	end
	h=(tf-t0)/n
	[t,x] = heun(f,x0,t0,tf,n,par)
end