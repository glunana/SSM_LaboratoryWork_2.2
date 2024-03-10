import numpy as np

def f(x):
    return np.sqrt(x)

def lagrange_interpolation(X, Y, x):
    result = 0
    n = len(X)

    for i in range(n):
        term = Y[i]
        for j in range(n):
            if j != i:
                term = term * (x - X[j]) / (X[i] - X[j])
        result += term

    return result

def newton_interpolation(X, Y, x):
    result = Y[0]
    n = len(X)
    temp = np.zeros((n, n))

    for i in range(n):
        temp[i, 0] = Y[i]

    for i in range(1, n):
        for j in range(n - i):
            temp[j, i] = (temp[j + 1, i - 1] - temp[j, i - 1]) / (X[i + j] - X[j])

    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (x - X[j])
        result += temp[0, i] * term

    return result

X1 = np.array([0, 1.7, 3.4, 5.1])
Y1 = f(X1)

X2 = np.array([0, 1.7, 4.0, 5.1])
Y2 = f(X2)

X_star = 3

lagrange_result1 = lagrange_interpolation(X1, Y1, X_star)
newton_result1 = newton_interpolation(X1, Y1, X_star)

lagrange_result2 = lagrange_interpolation(X2, Y2, X_star)
newton_result2 = newton_interpolation(X2, Y2, X_star)

error_lagrange1 = np.abs(f(X_star) - lagrange_result1)
error_newton1 = np.abs(f(X_star) - newton_result1)

error_lagrange2 = np.abs(f(X_star) - lagrange_result2)
error_newton2 = np.abs(f(X_star) - newton_result2)

print("Діапазон 1:")
print("Метод Лагранжа:", lagrange_result1)
print("Метод Ньютона:", newton_result1)
print("Похибка Лагранжа:", error_lagrange1)
print("Похибка Ньютона:", error_newton1)
print()

print("Діапазон 2:")
print("Метод Лагранжа:", lagrange_result2)
print("Метод Ньютона:", newton_result2)
print("Похибка Лагранжа:", error_lagrange2)
print("Похибка Ньютона:", error_newton2)
