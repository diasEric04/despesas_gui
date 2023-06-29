from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
from styles import setupTheme
from despesaForm import DespesaForm

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    setupTheme()

    despesaForm = DespesaForm()
    window.vLayout.addLayout(despesaForm)

    window.adjustFixedSize()
    window.show()
    app.exec()
