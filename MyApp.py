from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowExtension import MainWindowExtension

app=QApplication([])
myWindow= MainWindowExtension()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()