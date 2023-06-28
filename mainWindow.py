from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # basic window config
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

    def addWidgetToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def newDialogBox(self):
        return QMessageBox(self)
