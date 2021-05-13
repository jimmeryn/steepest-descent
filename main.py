import sys
from PyQt5 import QtWidgets
from ui.ui import MainWindow as UiWindow
from ui.gui import MainWindow as GuiWindow


def main():
    a = 2
    if a == 1:
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        window = GuiWindow()
        window.show()
        sys.exit(app.exec_())

    if a == 2:
        app = QtWidgets.QApplication(sys.argv)
        win = UiWindow()
        win.show()
        sys.exit(app.exec_())

    return 0


if __name__ == "__main__":
    main()
