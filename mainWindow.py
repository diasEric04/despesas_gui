from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtCore import Slot
from styles import getTheme, setTheme


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # basic window config
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        self.setMaximumWidth(800)

        self.menu = self.menuBar()
        self.themeMenu = self.menu.addMenu('Temas')

        self.theme = getTheme()

        self.lightTheme = self.themeMenu.addAction('menu "Light"')
        self.lightTheme.setCheckable(True)
        if self.theme == 'light':
            self.lightTheme.setChecked(True)
        slot = self.__makeSlot(self.__setLightTheme)
        self.lightTheme.toggled.connect(slot)

        self.darkTheme = self.themeMenu.addAction('menu "Dark"')
        self.darkTheme.setCheckable(True)
        if self.theme == 'dark':
            self.darkTheme.setChecked(True)
        slot = self.__makeSlot(self.__setDarkTheme)
        self.darkTheme.toggled.connect(slot)

    def addWidgetToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def newDialogBox(self):
        return QMessageBox(self)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def __makeSlot(self, func, *args, **kwargs):
        @Slot()
        def slot():
            func(*args, **kwargs)
        return slot

    def __setLightTheme(self):
        if self.theme == 'light':
            self.lightTheme.blockSignals(True)
            self.lightTheme.setChecked(True)
            self.lightTheme.blockSignals(False)
            self.__showWarnBox('"light theme" ja está em uso')
            return
        confirmation = self.__showConfirmBox(
            'Você deseja trocar o tema para "light"?'
        )
        if confirmation:
            setTheme('light')
            self.close()
        self.lightTheme.blockSignals(True)
        self.lightTheme.setChecked(False)
        self.lightTheme.blockSignals(False)

    def __setDarkTheme(self):
        if self.theme == 'dark':
            self.darkTheme.blockSignals(True)
            self.darkTheme.setChecked(True)
            self.darkTheme.blockSignals(False)
            self.__showWarnBox('"dark theme" ja está em uso')
            return
        confirmation = self.__showConfirmBox(
            'Você deseja trocar o tema para "dark"?'
        )
        if confirmation:
            setTheme('dark')
            self.close()
        self.darkTheme.blockSignals(True)
        self.darkTheme.setChecked(False)
        self.darkTheme.blockSignals(False)

    def __showWarnBox(self, text):
        dialogBox = self.newDialogBox()
        dialogBox.setText(text)
        dialogBox.setIcon(dialogBox.Icon.Warning)
        dialogBox.exec()

    def __showConfirmBox(self, text):
        dialogBox = self.newDialogBox()
        dialogBox.setText(text)
        dialogBox.setIcon(dialogBox.Icon.Question)
        dialogBox.setInformativeText(
            'lembre-se que ao trocar de tema o programa encerará e deverá'
            ' reabri-lo.'
        )
        dialogBox.setStandardButtons(
            dialogBox.StandardButton.Ok |
            dialogBox.StandardButton.Cancel
        )
        buttonClicked = dialogBox.exec()

        return buttonClicked == dialogBox.StandardButton.Ok
