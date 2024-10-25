import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.widgets import TextBox, Button, RadioButtons
class CalculadoraTrabajo:
    def __init__(self):
        # Crear figura con subplots horizontales
        self.fig = plt.figure(figsize=(15, 8))
        gs = self.fig.add_gridspec(2, 2, height_ratios=[4, 1])
        self.ax1 = self.fig.add_subplot(gs[0, 0])
        self.ax2 = self.fig.add_subplot(gs[0, 1])
        # Ajustar espaciado para widgets
        plt.subplots_adjust(bottom=0.25)
        # Configuración inicial
        self.x = np.linspace(0, 10, 1000)
        self.funcion_actual = "x**2"  # Placeholder
        self.limite_inferior = 0
        self.limite_superior = 5
        self.resultado_text = None
        # Inicializar gráficos
        self.line_fuerza, = self.ax1.plot([], [], 'b-', label='Fuerza')
        self.area = None
        self.ax1.set_title('Función de Fuerza')
        self.ax1.set_xlabel('Distancia (m)')
        self.ax1.set_ylabel('Fuerza (N)')
        self.ax1.grid(True)
        self.ax2.set_title('Trabajo Acumulado')
        self.ax2.set_xlabel('Distancia (m)')
        self.ax2.set_ylabel('Trabajo (J)')
        self.ax2.grid(True)
        # Agregar widgets de control
        self.crear_widgets()
        # Actualizar plot inicial
        self.actualizar_plot()
    def crear_widgets(self):
        # Función de fuerza
        axbox_funcion = plt.axes([0.1, 0.1, 0.3, 0.075])
        self.text_funcion = TextBox(axbox_funcion, 'F(x) = ', initial=self.funcion_actual)
        self.text_funcion.on_submit(self.actualizar_funcion)
        # Límites de integración
        axbox_li = plt.axes([0.5, 0.1, 0.1, 0.075])
        axbox_ls = plt.axes([0.7, 0.1, 0.1, 0.075])
        self.text_li = TextBox(axbox_li, 'x inicial = ', initial=str(self.limite_inferior))
        self.text_ls = TextBox(axbox_ls, 'x final = ', initial=str(self.limite_superior))
        self.text_li.on_submit(self.actualizar_limites)
        self.text_ls.on_submit(self.actualizar_limites)
        # Calculo
        axbutton = plt.axes([0.85, 0.1, 0.1, 0.075])
        self.button = Button(axbutton, 'Calcular')
        self.button.on_clicked(self.calcular_trabajo)
    def funcion_fuerza(self, x):
        try:
            return eval(self.funcion_actual)
        except:
            return np.zeros_like(x)
    def actualizar_funcion(self, texto):
        self.funcion_actual = texto
        self.actualizar_plot()
    def actualizar_limites(self, texto):
        try:
            self.limite_inferior = float(self.text_li.text)
            self.limite_superior = float(self.text_ls.text)
            self.actualizar_plot()
        except ValueError:
            pass
    def actualizar_plot(self):
        # Actualizar gráfico de fuerza
        x_plot = np.linspace(min(0, self.limite_inferior), max(10, self.limite_superior), 1000)
        self.line_fuerza.set_data(x_plot, self.funcion_fuerza(x_plot))
        # Actualizar límites de los ejes
        self.ax1.relim()
        self.ax1.autoscale_view()
        # Limpiar área sombreada
        if self.area is not None:
            self.area.remove()
        # Crear nueva área sombreada
        x_area = np.linspace(self.limite_inferior, self.limite_superior, 100)
        self.area = self.ax1.fill_between(x_area, self.funcion_fuerza(x_area), alpha=0.3)
        # Actualizar gráfico de trabajo acumulado
        x_trabajo = np.linspace(self.limite_inferior, self.limite_superior, 100)
        trabajo_acumulado = [integrate.quad(self.funcion_fuerza, self.limite_inferior, x)[0] for x in x_trabajo]
        self.ax2.clear()
        self.ax2.plot(x_trabajo, trabajo_acumulado, 'g-', label='Trabajo Acumulado')
        self.ax2.set_title('Trabajo Acumulado')
        self.ax2.set_xlabel('Distancia (m)')
        self.ax2.set_ylabel('Trabajo (J)')
        self.ax2.grid(True)
        # Limpiar texto
        if self.resultado_text:
            self.resultado_text.remove()
            self.resultado_text = None
        plt.draw()
    def calcular_trabajo(self, event):
        try:
            trabajo, error = integrate.quad(self.funcion_fuerza, self.limite_inferior, self.limite_superior)
            # Limpiar texto
            if self.resultado_text:
                self.resultado_text.remove()
            # Nuevo texto
            self.resultado_text = plt.figtext(0.1, 0.02, f'Trabajo total = {trabajo:.2f} Joules', 
                                           bbox=dict(facecolor='white', edgecolor='black', alpha=0.7))
        except:
            if self.resultado_text:
                self.resultado_text.remove()
            self.resultado_text = plt.figtext(0.1, 0.02, 'Error en el cálculo', 
                                           bbox=dict(facecolor='red', edgecolor='black', alpha=0.7))
        plt.draw()

def main():
    calculadora = CalculadoraTrabajo()
    plt.show()
if __name__ == "__main__":
    main()