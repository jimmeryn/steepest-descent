from ui.canvas import Canvas
from testFunctions import TestFunctions
from mns import mns
from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets
from functionStringParser import function_string_parser
import sympy as sp
from errorhandlers.ProblemSizeError import ProblemSizeError


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Metoda Najszybszego Spadku")
        self.connectButtons()

    def handleOnStart(self):
        line_func = self.ui.lineEdit_function.text()
        line_iter = self.ui.lineEdit_iteration.text()
        line_start_vec = self.ui.lineEdit_start_vector.text()
        line_step_size = self.ui.lineEdit_step_size.text()
        line_stop_term = self.ui.lineEdit_stop_term.text()
        line_test = self.ui.lineEdit_test.text()
        try:
            start_vec = sp.Matrix(list(map(lambda x: float(x), list(line_start_vec.split(", ")))))
        except:
            self.addLog("Blad w punkcie poczatkowym")
            return
        self.ui.textEdit_output.setText("")
        result = None
        try:
            result = mns(
                start_vec,
                float(line_stop_term),
                int(line_iter),
                float(line_test),
                float(line_step_size),
                line_func,
                self.addLog,
            )
        except ProblemSizeError as e:
            self.addLog(str(e))
            return

        points = list(map(lambda point: [point[0], point[1]], result["points"]))
        x2 = list(map(lambda point: point[0], points))
        y2 = list(map(lambda point: point[1], points))
        try:
            self.addCanvas(line_func, x2, y2)
        except:
            self.addLog("Wymiar problemu > 2")

    def addLog(self, log: str):
        self.ui.textEdit_output.append("\n" + log)

    def addCanvas(self, line_func: str, x2, y2):
        func = function_string_parser(line_func)
        sc = Canvas(self, fun=func, width=5, height=4, dpi=100, x2=x2, y2=y2)
        layout = self.ui.groupBox_3.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout()

        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()

        layout.addWidget(sc)
        self.ui.groupBox_3.setLayout(layout)

    def connectButtons(self):
        self.ui.pushButton_start_algorythm.clicked.connect(self.handleOnStart)
        self.ui.pushButton_Geem.clicked.connect(self.handleFunctionGeemButtonClick)
        self.ui.pushButton_Goldstei_Pirce.clicked.connect(self.handleFunctionPriceButtonClick)
        self.ui.pushButton_Himmelblau.clicked.connect(self.handleFunctionHimButtonClick)
        self.ui.pushButton_test_function.clicked.connect(self.handleFunctionTestButtonClick)

    def handleFunctionHimButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.modified_himmelblau_function())

    def handleFunctionPriceButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.goldstein_price_function())

    def handleFunctionGeemButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.geem_function())

    def handleFunctionTestButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.test_function())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
