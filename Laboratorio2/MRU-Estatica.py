import numpy as np
import matplotlib.pyplot as plt
# Constantes
G = 6.67430e-11  # Constante gravitacional 
M = 1.989e30     # Masa del sol
R = 1.496e11     # Radio de la órbita terrestre
def velocidad_orbital(M, R):
    return np.sqrt(G * M / R)
v_orbital = velocidad_orbital(M, R)
# Gráfica de la órbita circular
theta = np.linspace(0, 2 * np.pi, 100)
x = R * np.cos(theta)
y = R * np.sin(theta)

print(f"Velocidad orbital del planeta: {v_orbital:.2f} m/s")
plt.figure(figsize=(6,6))
plt.plot(x, y, label='Órbita del planeta')
plt.scatter(0, 0, color='yellow', label='Sol', s=200)  
plt.title('Órbita del planeta alrededor del Sol')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

