import matplotlib
import numpy as np

matplotlib.use("Qt5Agg")
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui.ui_data import inputs, button_labels
from functionStringParser import function_string_parser
from testFunctions import TestFunctions


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


def say_hello():
    print("Button clicked, Hello!")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        func = function_string_parser(TestFunctions.modified_himmelblau_function())
        print(func)
        sc = Canvas(self, fun=func, width=5, height=4, dpi=100)

        layout = QtWidgets.QHBoxLayout()
        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()
        layout3 = QtWidgets.QVBoxLayout()
        layout4 = QtWidgets.QVBoxLayout()
        group1 = QtWidgets.QGroupBox("Menu")
        group2 = QtWidgets.QGroupBox("Wejście")
        group3 = QtWidgets.QGroupBox("Wizualizacja")
        group4 = QtWidgets.QGroupBox("Logs")

        for label in button_labels:
            button = QtWidgets.QPushButton(label)
            button.clicked.connect(say_hello)
            layout1.addWidget(button)
        for input in inputs:
            layout2.addWidget(QtWidgets.QLabel(input["label"]))
            layout2.addWidget(QtWidgets.QLineEdit(input["defaultInput"]))

        layout4.addWidget(QtWidgets.QTextEdit())

        group1.setLayout(layout1)
        group2.setLayout(layout2)
        layout3.addWidget(sc)
        group3.setLayout(layout3)
        group4.setLayout(layout4)

        for group in [group1, group2, group3, group4]:
            layout.addWidget(group)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
