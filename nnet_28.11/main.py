import numpy as np
import scipy
from scipy import special

I = np.array([0.9, 0.1, 0.8], ndmin=2).T
t = np.array([0.1, 0.4, 0.9], ndmin=2).T

W_i_h = np.array([[0.9, 0.3, 0.4],
                  [0.2, 0.8, 0.2],
                  [0.1, 0.5, 0.6]])

W_h_o = np.array([[0.3, 0.7, 0.5],
                  [0.6, 0.5, 0.2],
                  [0.8, 0.1, 0.9]])

for i in range(1000):
    X_h = W_i_h.dot(I)
    O_h = scipy.special.expit(X_h)
    X_o = W_h_o.dot(O_h)
    O = scipy.special.expit(X_o)

    E_o = t - O
    E_h = np.dot(W_h_o.T, E_o)

    W_h_o += 0.2 * E_o * O * (1 - O) * O_h.T
    W_i_h += 0.2 * E_h * O_h * (1 - O_h) * I.T

print(O)

