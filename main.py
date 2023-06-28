from PySide6.QtWidgets import QApplication, QPushButton
from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()

    buttonTeste = QPushButton('botao de teste')
    buttonTeste.clicked.connect(lambda: print('botao clicado'))
    window.addWidgetToLayout(buttonTeste)

    window.show()
    app.exec()
