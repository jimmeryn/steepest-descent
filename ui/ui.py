from ui.canvas import Canvas
from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Metoda Najszybszego Spadku")
    def addCanvas(self, line_func: str):
        func = function_string_parser(line_func)
        sc = Canvas(self, fun=func, width=5, height=4, dpi=100)
        layout = qtw.QVBoxLayout()
        layout.addWidget(sc)
        self.ui.groupBox_3.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    win = qtw.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())