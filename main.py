from PySide6.QtWidgets import QApplication, QPushButton
from mainWindow import MainWindow
import data
from styles import setupTheme

if __name__ == '__main__':
    DATA_FOLDER = data.initData()

    app = QApplication()
    window = MainWindow()
    setupTheme(DATA_FOLDER)

    buttonTeste = QPushButton('botao de teste')
    buttonTeste.clicked.connect(lambda: print('botao clicado'))
    window.addWidgetToLayout(buttonTeste)

    window.show()
    app.exec()
