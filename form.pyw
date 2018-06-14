from PyQt5 import QtCore, QtGui, QtWidgets
import workdays

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Расчет Пени")
        MainWindow.resize(488, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(11, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setFrame(True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 13), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 30))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2018, 6, 13))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setFrame(True)
        self.dateEdit_2.setDate(QtCore.QDate(2018, 6, 13))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(7999, 12, 30))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2018, 6, 13))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 141, 41))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setButtonSymbols(1)
        self.lineEdit.setValue(0)
        self.lineEdit.setSuffix(' грн')
        self.lineEdit.setDecimals(2)
        self.lineEdit.setRange(0.0,9999999999999)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 171, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.lineEdit_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 270, 451, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setButtonSymbols(2)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setSuffix(' грн')
        self.lineEdit_2.setValue(0)
        self.lineEdit_2.setDecimals(2)


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 171, 21))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Дата начала задолженности  "))
        self.label_2.setText(_translate("MainWindow", "Дата расчета "))
        self.label_3.setText(_translate("MainWindow", "Сумма долга"))
        self.pushButton.setText(_translate("MainWindow", "Расчитать"))
        self.label_4.setText(_translate("MainWindow", "Результат"))

    def on_click(self):
        result = self.debt_fine(self.get_dept_days())
        self.lineEdit_2.setValue(result)




    def get_dept_days(self):
        must_payment_day = QtCore.QDate.toPyDate(self.dateEdit.date())
        payment_day = QtCore.QDate.toPyDate(self.dateEdit_2.date())
        dept_days = abs((workdays.networkdays(payment_day, must_payment_day)))
        return dept_days



    def debt_fine(self, dept_days):
        dept_value = self.lineEdit.value()
        stavka = 2*17
        sum = dept_value * 2 * stavka / 100 / 365 * dept_days
        return sum





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

