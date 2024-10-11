import numpy as np
import matplotlib.pyplot as plt
# Parámetros del problema
m = 2.0  # masa
vi = 2.0  # velocidad inicial 
vf = 10.0  # velocidad final 
d = 20.0  # distancia recorrida 
t = 5.0   # tiempo total 
# Aceleración promedio
a = (vf - vi) / t
# Fuerza = masa * aceleración
fuerza = m * a
# Cálculo del movimiento
tiempo = np.linspace(0, t, 100)
velocidad = vi + a * tiempo
distancia = vi * tiempo + 0.5 * a * tiempo**2
print(f"Aceleración promedio: {a:.2f} m/s²")
print(f"Fuerza aplicada: {fuerza:.2f} N")
plt.figure(figsize=(10, 5))
# Velocidad
plt.subplot(1, 2, 1)
plt.plot(tiempo, velocidad, label='Velocidad (m/s)', color='blue')
plt.title('Velocidad vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
# Distancia
plt.subplot(1, 2, 2)
plt.plot(tiempo, distancia, label='Distancia (m)', color='green')
plt.title('Distancia vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Distancia (m)')
plt.grid(True)
plt.tight_layout()
plt.show()

