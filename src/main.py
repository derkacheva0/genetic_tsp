import sys
from Mediator import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    mediator = Mediator(ui)

    MainWindow.show()
    sys.exit(app.exec_())
