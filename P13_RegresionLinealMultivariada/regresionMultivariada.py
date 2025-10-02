import numpy as np

X1 = [-6,	-4,	7,	4,	7,	-3,	-4,	8,	3,	4,	-6,	4,	-5,	10,	10]
X2 =[	-2,	5,	4,	8,	0,	-6,	5,	1,	9,	6,	3,	-10,	0,	1,	-3]
Yobservada	= [-20,	4,	31,	30, 24	,-15,	1,	32, 32,	28,	-9,	-2,	-9,	34,	29]

X = []
for i in range(len(X1)):
    X.append([1, X1[i], X2[i]])

X1 = np.array(X1)
X2 = np.array(X2)
X = np.array(X) #arreglo de numpy...
Y = np.array(Yobservada)

XtX = X.T.dot(X)
XtX_inv = np.linalg.inv(XtX)
temp = XtX_inv.dot(X.T)
b_estimada = temp.dot(Y)

print("b: ", b_estimada)

Yestimada = X.dot(b_estimada)

print(Yestimada)

from matplotlib import pyplot as plt
x1_grid = np.linspace(X1.min(), X1.max(), 30)
x2_grid = np.linspace(X2.min(), X2.max(), 30)
X1g, X2g = np.meshgrid(x1_grid, x2_grid)
Yg = b_estimada[0] + b_estimada[1] * X1g + b_estimada[2] * X2g

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X1, X2, Y, alpha=0.7)
ax.plot_surface(X1g, X2g, Yg, rstride=1, cstride=1, alpha=0.3)
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("y")
ax.set_title("Regresión lineal 3D: puntos y plano ajustado")
plt.tight_layout()
plt.show()

from P12_RegresionLineal import main_MetricasError as calc
rmse = calc.rmse(Y, Yestimada)
print(rmse)