function MAIN ()
L = 5;
ganancia = 0.1;
h = ganancia*(1+randn(L,1));
%sigma = 0;
%sigma = 0.1;
%sigma = 1;
%sigma = 10;
%sigma = 20;
%sigma = 50;
sigma = 100;

a = imread('lena512.bmp');
M = size(a,2);
P = size(a,1);
H = toeplitz([h.' zeros(1,M-L)],zeros(1,M));
r = zeros(M,P);
N = sigma*randn(M,P); %Noise
s = double(a(:,:)); % 
r = H*s + N; % lo que se recibe
b = uint8(r);
figure(1),title('Ejercicio 1,2')
subplot(1,2,1), imshow(a),title('Original') % muestro la imagen original
subplot(1,2,2), imshow(b),title('Recibida') % muestro la imagen recibida

E = 1024;
%E = 512;
%E = 32;
sE= zeros(E,1);
for i=1:E
    sE(i,1) = rand()*256-1;
end
ME= size(sE,1);
PE= size(sE,2);
HE= toeplitz([h.' zeros(1,ME-L)],zeros(1,ME));
rE= zeros(ME,PE);
NE= sigma*randn(ME,PE); % ruido
% se transmite
rE = HE*sE + NE; % lo que se recibe
% estimo h
S = toeplitz(sE');
S = S(:,1:L);
S = tril(S);
he = estimate(S,rE);
%comparo h con h estimado
% estimo la imagen
He= toeplitz([he.' zeros(1,M-L)],zeros(1,M));
CN= sigma^2*eye(size(He)); % matriz de covarianza del ruido
sigmax= sqrt(1/256*(sum(((0:255)-mean(0:255)).^2))); %
%dispersi´on de los s´imbolos enviados
mx= mean(0:255)*ones(M,1); % media de los s´imbolos enviados
CX= sigmax^2*eye(size(He)); % matriz de covarianza de los
%simbolos enviados - asume independencia
W = CX*He'*inv(He*CX*He'+CN); % matriz de ecualizaci´on
d = zeros(M,P);
for k = 1:P
d(:,k) = W*(r(:,k)-He*mx)+mx;
end
d = uint8(d);
figure(2),title('Ejercicio 3')
subplot(1,3,1), imshow(a),title('Original')  % muestro la imagen original
subplot(1,3,2), imshow(b),title('Recibida') % muestro la imagen recibida
subplot(1,3,3), imshow(d),title('Estimada') % muestro la imagen estimada

