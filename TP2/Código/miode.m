function [t,x] = miode(f,x0,t0,tf,dtmax,tol,par)
	n = ceil((tf-t0)/dtmax);
	error = 10; %Para que entre al while
	while(error>tol)
		[t1,x1]=heun(f,x0,t0,tf,n,par);
		[t2,x2]=heun(f,x0,t0,tf,2*n,par);
		error = abs(x1(end,:)- x2(end,:));
		n = n+1;
	end
	h =(tf-t0)/n;
	[t,x] = heun(f,x0,t0,tf,n,par);
end
