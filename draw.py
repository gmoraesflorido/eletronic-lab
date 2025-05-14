import numpy as np
import matplotlib.pyplot as plt
from math import exp

# Constantes do circuito
V_plus = 1.0           # Tensão da fonte (V)
R = 1e3                # Resistência (Ohms)
IS = 1e-15             # Corrente de saturação do diodo (A)
VT = 0.025             # Tensão térmica (V)

# Pontos calculados
vd_pontos = np.array([0.5, 0.6, 0.65, 0.68, 0.7, 0.72, 0.75])
id_pontos = np.array([IS * (exp(v / VT) - 1) for v in vd_pontos])

Vd = np.linspace(0.0, 1, 400)
Id_diodo = IS * (np.exp(Vd / VT) - 1)
Id_carga = (V_plus - Vd) / R


plt.figure(figsize=(10, 6))
plt.plot(Vd, Id_diodo * 1e6, label='Curva do diodo (exponencial)', color='red')
plt.plot(Vd, Id_carga * 1e6, label='Reta de carga', color='blue')
plt.scatter(vd_pontos, id_pontos * 1e6, color='black', label='Pontos estimados')

plt.xlabel('Tensão no diodo (V)')
plt.ylabel('Corrente (µA)')
plt.title('Reta de carga e curva do diodo')
plt.grid(True)
plt.legend()
plt.ylim(0, 3000)
plt.yticks(np.arange(0, 3001, 250))
plt.tight_layout()
plt.show()
