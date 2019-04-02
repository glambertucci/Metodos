import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz


class Metodos:

    def __init__(self, dev):#standard deviation
        self.L = 5
        self.gain = 0.1
        self.h = self.gain * (1 + np.random.randn(self.L, 1))
        self.dev = dev

        self.a = plt.imread("lena512.bmp")#loads the pic

        #col and fil size
        self.M = len(self.a[:, 1])
        self.P = len(self.a[1, :])

        self.H = toeplitz(np.concatenate((np.transpose(self.h), np.zeros(self.M-self.L)), axis=None), np.zeros(self.M)) #Impulse response
        self.N = self.dev*np.random.randn(self.M, self.P)#Noise
        self.s = self.a.astype(float)#input

        self.r = np.zeros((self.M, self.P))
        self.r = (self.H.dot(self.s))+self.N
        self.b = self.r.astype(int) #output

        plt.figure(1)
        plt.subplot(1,2,1)#loads the plots
        plt.imshow(self.a,cmap='gray',vmin=1,vmax=255)
        plt.subplot(1,2,2)
        plt.imshow(self.b,cmap='gray',vmin=1,vmax=255)

    def show_graph(self):
        plt.show()

    def singular_values(self, ent):#ent Training 2define
        pass