from PyQt5 import QtCore, QtGui, QtWidgets


class MainApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Calculation App'
        self.window_width = 400
        self.window_high = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.window_width, self.window_high)
        self.show()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())