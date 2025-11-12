from MainWindow import Ui_MainWindow


class MyMainExtension(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlots()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalandSlots(self):
        self.pushButtonClose.clicked.connect(self.process_close)
        self.pushButtonClear.clicked.connect(self.process_clear)
    def process_close(self):
        self.MainWindow.close()
    def process_clear(self):
        self.lineEditA.clear()
        self.lineEditB.clear()
        self.lineEditC.clear()
        self.lineEditResult.clear()
        self.lineEditA.setFocus()


