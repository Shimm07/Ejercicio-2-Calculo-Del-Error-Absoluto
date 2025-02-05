# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gVckOumObaFP3Q3hZSgyxHYzH_b5-6sL
"""

#   Codigo que implementa un esquema numerico
#   para determinar la aproximacion de Leibniz
#
#           Autor:
#   Angel Gabriel Chim Vera
#   angchimvera@gmail.com
#   Version 1.0 : 04/02/2025
#

import numpy as np  # Se importa numpy para cálculos numéricos
import matplotlib.pyplot as plt  # Se importa matplotlib para graficar

# Función que implementa la serie de Leibniz para aproximar pi
def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi  # Valor real de pi
N_values = [10, 100, 1000, 10000]  # Diferentes valores de N para la aproximación
errors_abs = []  # Lista para almacenar los errores absolutos
errors_rel = []  # Lista para almacenar los errores relativos
errors_sq = []   # Lista para almacenar los errores cuadráticos

# Iterar sobre los valores de N para calcular las aproximaciones y errores
for N in N_values:
    approx_pi = leibniz_pi(N)  # Aproximación de pi con N términos
    error_abs = abs(true_pi - approx_pi)  # Error absoluto
    error_rel = error_abs / true_pi  # Error relativo
    error_sq = error_abs**2  # Error cuadrático
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_sq.append(error_sq)
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}, Error cuadrático={error_sq}")

# Representación gráfica de los errores
plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_sq, label='Error cuadrático', marker='^')
plt.xscale('log')  # Escala logarítmica en el eje x
plt.yscale('log')  # Escala logarítmica en el eje y
plt.xlabel('N')  # Etiqueta del eje x
plt.ylabel('Error')  # Etiqueta del eje y
plt.legend()  # Agregar leyenda a la gráfica
plt.title('Errores en la aproximación de pi')  # Título de la gráfica
plt.show()