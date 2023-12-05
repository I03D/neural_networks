import math

def sigma(X):
    return 1 / (1 + math.exp(-X))

def f_activate(X):
    return [sigma(x) for x in X]
    # return 1 / (1 + math.exp(-x))

def mult(W, I):
    W_rows = len(W)
    W_cols = len(W[0])
    I_rows = len(I)

    if W_cols != I_rows:
        print('Количество столбцов первой матрицы не равно количеству строк второй матрицы!')
        return

    X = [0 for col in range(W_rows)]
    O = [0 for col in range(W_rows)]

    for i in range(W_rows):
        for j in range(W_cols):
            X[i] += W[i][j] * I[j]
        O = f_activate(X)
    
    return O

# class Neuron:
#     def __init__(self, w1, w2):
#         self.w1 = w1
#         self.w2 = w2
# 
#     def forward(self, x1, x2):
#         summ = x1 * self.w1 + x2*self.w2
#         return f_activate(summ)

A = [
        [0.9, 0.3, 0.4],
        [0.2, 0.8, 0.2],
        [0.1, 0.5, 0.6]
    ] 
B = [0.9, 0.1, 0.8]

C = mult(A, B)
print(C)

# n1 = Neuron(0.9, 0.3)
# n2 = Neuron(0.2, 0.8)
# print(n1.forward(1.0, 0.5))
# print(n2.forward(1.0, 0.5))

