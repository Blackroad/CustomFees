from PyQt5 import QtCore, QtGui, QtWidgets
import workdays

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Test')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")


        # Календарик №1
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
        # Календарик №2
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

        # Поле сумма задожености
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

        # Лейбла для сумма задолжености
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 171, 21))
        self.label_3.setObjectName("label_3")

        # Кнопка Рассчитать
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        # Поле Результат
        self.lineEdit_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 270, 431, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setButtonSymbols(2)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setSuffix(' грн')
        self.lineEdit_2.setValue(0)
        self.lineEdit_2.setDecimals(2)
        self.lineEdit_2.setRange(0,9999999999999999)
        # Поле Ставка НБУ
        self.lineEdit_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 20, 141, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setButtonSymbols(1)
        self.lineEdit_3.setSuffix(' %')
        self.lineEdit_3.setValue(0)
        self.lineEdit_3.setDecimals(1)
        self.lineEdit_3.setSingleStep(0.5)

        #Лейбла для Рузультата
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 171, 21))
        self.label_4.setObjectName("label_4")
        # Лейбла для Поля ставка НБУ
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 0, 171, 21))
        self.label_5.setObjectName("label_5")
        self.label_5.setText('Ставка НБУ')
        # Переключатель
        self.box = QtWidgets.QGroupBox("Множитель ставки",self.centralwidget)
        self.box.setGeometry(QtCore.QRect(300, 90, 130, 130))
        self.radio = QtWidgets.QRadioButton(' x1',self.box)
        self.radio1 = QtWidgets.QRadioButton(' x2',self.box)
        self.radio.setChecked(True)
        self.radio.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.radio1.setGeometry(QtCore.QRect(10, 40, 171, 21))

      # TODO Добавить ставку по кредиту (но не более 2% НБУ)
      # TODO Дабвить Праздники
      # TODO Сделать сервис по получению ставки НБУ

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
        try:
            if must_payment_day > payment_day:
                self.window = QtWidgets.QMessageBox.information(self.centralwidget,
                                                                'Внимание!',
                                                                'Дата начала задолжености'
                                                                ' не может быть больше даты расчета!',
                                                                buttons=QtWidgets.QMessageBox.Ok)
        finally:
                dept_days = abs((workdays.networkdays(payment_day, must_payment_day)))
                return dept_days

    def get_multiplicator(self):
        multiple = None
        if self.radio.isChecked() == True:
            multiple = 1
        elif self.radio1.isChecked() == True:
            multiple = 2
        return (multiple)

    def debt_fine(self, dept_days):
        multiple = self.get_multiplicator()
        dept_value = self.lineEdit.value()
        stavka = self.lineEdit_3.value() * multiple
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

