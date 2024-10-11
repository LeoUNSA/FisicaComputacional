# Primer ejercicio - Desplazamiento
def desplazamientov1(v, delta_t):
    return v * delta_t
# Segundo ejercicio - Desplazamiento v2
def desplazamientov2(vi, alpha, delta_t):
    return vi * delta_t + (alpha * delta_t**2) / 2
# Tercer ejercicio - Velocidad final
def velocidadFinal(vi, alpha, delta_t):
    return vi + alpha * delta_t
def ask4input(num):
    return float(input(num))
# Solicitar entradas al usuario
v = ask4input("Velocidad: ")
vi = ask4input("Velocidad inicial: ")
alpha = ask4input("Aceleracion: ")
delta_t = ask4input("Tiempo: ")
# Resultados
delta_x_a = desplazamientov1(v, delta_t)
delta_x_b = desplazamientov2(vi, alpha, delta_t)
vf = velocidadFinal(vi, alpha, delta_t)
# Print
print(f"\nResultados:")
print(f"Desplazamiento (ecuación a): {delta_x_a} m")
print(f"Desplazamiento (ecuación b): {delta_x_b} m")
print(f"Velocidad final (ecuación c): {vf} m/s")
