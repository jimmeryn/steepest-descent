import matplotlib
import numpy as np

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Canvas(FigureCanvas):
    def __init__(self, parent=None, fun=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)

        """
        Matplotlib Script
        """
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = fun(X, Y)
        self.ax.contourf(X, Y, Z, 20, cmap="RdYlGn")
        super(Canvas, self).__init__(fig)
