from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication()
my_gui=MyMainExtension()
my_gui.setupUi(QMainWindow())
my_gui.showWindow()
app.exec()