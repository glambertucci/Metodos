import metodos as Mt

import numpy as np

#yuyin = Mt.Metodos(0.1)
#yuyin.calculate()
#yuyin.show_graph()

A = [[1, 2, 3], [5, 6, 7], [8, 9, 10], [11, 12, 13]]
B = np.transpose(A) * A
avas, aves = np.linalg.eig(B)

dictionary = {}
for i in avas:
    dictionary.setdefault(avas[i], aves[:, i])

avas.sort(True)
aves_sorted = [[], []]

for i in avas:
    aves_sorted[:, i] = dictionary.setdefault(i)

singular = np.sqrt(avas)
sigma = np.diag(singular)

U = A * avas / singular

Vt = np.transpose(aves)
print(U, sigma, Vt)

U2, sigma2, Vt2 = np.linalg.svd(A, full_matrices=False)

print(U2, sigma2, Vt2)