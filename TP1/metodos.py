import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz


class Metodos:

    def __init__(self, dev):
        self.dev = dev
#       standard deviation
        self.a = plt.imread("lena512.bmp")
#       loads the pic
        self.b = 0
        self.l = 5
        self.gain = 0.1
        self.h = self.gain * (1 + np.random.randn(self.l, 1))

    def calculate(self):
#       col and fil size
        self.m = len(self.a[:, 1])
        self.p = len(self.a[1, :])

        H = toeplitz(np.concatenate((np.transpose(self.h), np.zeros(self.m-self.l)), axis=None), np.zeros(self.m))
#       Impulse response
        n = self.dev*np.random.randn(self.m, self.p)
#       Noise
        s = self.a.astype(float)
#       input
        self.r = (H.dot(s))+n
        self.b = self.r.astype(int)
#       output

    def show_graph(self):
        plt.figure(1)
        plt.subplot(1, 2, 1)
#       loads the plots
        plt.imshow(self.a, cmap='gray', vmin=0, vmax=255)
        plt.subplot(1, 2, 2)
        plt.imshow(self.b, cmap='gray', vmin=0, vmax=255)
        plt.show()

    def singular_values(self):
#       ent Training 2define
        pass

    def ej_2(self, ent):
        E = ent
        LE=1
        sE = -1 + np.random.uniform(0, 256, [E, LE])
#        print(sE)
        HE = toeplitz(np.concatenate((np.transpose(self.h), np.zeros(E-self.l)), axis=None), np.zeros(E))
        ne = self.dev*np.random.randn(E, LE)
        rE = HE.dot(sE)+ne

        hesv = self.singular_values()
        He= toeplitz(np.concatenate((np.transpose(hesv), np.zeros(self.m-self.l)), axis=None), np.zeros(self.m))
#known Sequence
        CN = self.dev**2 * np.eye(np.size(He))
        temp = np.zeros(256)
        for i in range(0, 256):
            temp[i] = (i - 127.5) ** 2
        sigmax = np.sqrt(np.sum(temp) / 256)
        mx = np.mean(range(0,256)).dot(np.ones(self.m))
        CX = sigmax**2 * np.eye(np.size(He))
        W = CX.dot(np.transpose(He).dot(np.linalg.inv(He.dot(CX.dot(np.transpose(He))+CN))))
        self.d = np.zeros(self.m, self.p)
        for i in range(1,self.p):
            self.d[:, i] = W.dot(self.r[:,i]-He*mx) + mx
        self.d = self.d.astype(int)

    def show_graph2(self):
        plt.figure(2)
        plt.subplot(1, 3, 1)
        plt.imshow(self.a)
        plt.subplot(1, 3, 2)
        plt.imshow(self.b)
        plt.subplot(1, 3, 3)
        plt.imshow(self.d)

