# Максименко И-03
import numpy as np
import scipy
from scipy import special
# Максименко И-03

I = np.array([1.0, 0.5])

# Максименко И-03
W = np.array([[0.9, 0.3],
              [0.2, 0.8]])

# Максименко И-03
print(W)
O = W.dot(1) # Эта функция ничего не даёт. Видимо, просто копируется матрица весов.
print(O)
# Максименко И-03
O = scipy.special.expit(O) # Это функция активации.
print(O)

# Максименко И-03

