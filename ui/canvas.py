import matplotlib
import numpy as np

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Canvas(FigureCanvas):
    def __init__(self, parent=None, fun=None, width=5, height=4, dpi=100, x2=None, y2=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)

        """
        Matplotlib Script
        """
        x1 = np.linspace(-5, 5, 100)
        y1 = np.linspace(-5, 5, 100)

        try:
            X, Y = np.meshgrid(x1, y1)
            Z = fun(X, Y)
            self.ax.contourf(X, Y, Z, 20, cmap="RdYlGn")
            self.ax.plot(x2, y2, "o-k", linewidth=0.3, markersize=2)
            self.ax.plot(x2[-1], y2[-1], "ok", markersize=5, markerfacecolor="white")
        except:
            pass
        super(Canvas, self).__init__(fig)
