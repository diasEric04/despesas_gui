from PySide6.QtWidgets import QApplication, QPushButton
from mainWindow import MainWindow
import data
from styles import setupTheme
from despesaForm import DespesaForm

if __name__ == '__main__':
    DATA_FOLDER = data.initData()

    app = QApplication()
    window = MainWindow()
    setupTheme(DATA_FOLDER)

    despesaForm = DespesaForm()
    window.vLayout.addLayout(despesaForm)

    button1 = QPushButton('botao de teste 1')
    button1.clicked.connect(lambda: print('botao 1 clicado'))

    button2 = QPushButton('botao de teste 2')
    button2.clicked.connect(lambda: print('botao 2 clicado'))

    button3 = QPushButton('botao de teste 3')
    button3.clicked.connect(lambda: print('botao 3 clicado'))

    despesaForm.addWidgetToForm(button1, 0, 0)
    despesaForm.addWidgetToForm(button2, 0, 1)
    despesaForm.addWidgetToForm(button3, 1, 0, 1, 2)

    window.show()
    app.exec()
