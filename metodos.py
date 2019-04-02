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

    def calculate(self):
        l = 5
        gain = 0.1
        h = gain * (1 + np.random.randn(l, 1))
#       col and fil size
        m = len(self.a[:, 1])
        p = len(self.a[1, :])

        H = toeplitz(np.concatenate((np.transpose(h), np.zeros(m-l)), axis=None), np.zeros(m))
#       Impulse response
        n = self.dev*np.random.randn(m, p)
#       Noise
        s = self.a.astype(float)
#       input
        r = (H.dot(s))+n
        self.b = r.astype(int)
#       output

    def show_graph(self):
        plt.figure(1)
        plt.subplot(1, 2, 1)
#       loads the plots
        plt.imshow(self.a, cmap='gray', vmin=0, vmax=255)
        plt.subplot(1, 2, 2)
        plt.imshow(self.b, cmap='gray', vmin=0, vmax=255)
        plt.show()

    def singular_values(self, A):
        B = (np.transpose(A)).dot(A)
        avas, aves = np.linalg.eig(B)

        dictionary = {}
        for i in range(len(avas)):
            dictionary.setdefault(avas[i], aves[:, i])

        avas.sort()
        avas = np.flip(avas)
        aves_sorted = []

        for i in range(len(avas)):
            aves_sorted.append(dictionary.setdefault(avas[i]))

        singular = np.sqrt(avas)
        sigma = np.diag(singular)

        descartes, U = np.linalg.eig(np.asarray(A).dot(np.transpose(A)))

        Vt = np.transpose(aves)

        return [U, sigma, Vt]
