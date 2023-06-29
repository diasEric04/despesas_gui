from PySide6.QtWidgets import (QGridLayout, QWidget, QLineEdit, QPushButton,
                               QCheckBox, QLabel)
from PySide6.QtCore import Qt, Slot
from styles import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


# i
class FormInput(QLineEdit):
    def __init__(self, placeholder: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setPlaceholderText(placeholder)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(
            f'font-size: {MEDIUM_FONT_SIZE}px;'
            f'margin: 10px;'
        )
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        # left, top, right e bottom
        # [TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN] = V
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)


# c
class FormCheckbox(QCheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(
            f'font-size: {MEDIUM_FONT_SIZE}px;'
            f'text-align: right;'
        )
        self.setMinimumWidth(100)
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 2)


# b
class FormButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(
            f'font-size: {BIG_FONT_SIZE}px;'
        )
        self.setMinimumSize(100, 50)


class Spacement(QLabel):
    def __init__(self, margin: int):
        super().__init__()
        self.setStyleSheet(
            f'margin: {margin}px;'
        )


class DespesaForm(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__createMaskedWidgets()

    def __createMaskedWidgets(self):
        self.name = FormInput('Nome da despesa:')
        self.addWidgetToForm(self.name, 0, 0, 1, 2)

        self.type = FormInput('Tipo da despesa:')
        self.addWidgetToForm(self.type, 1, 0)

        self.monthPaymentDay = FormInput('Dia de pagamento p/mes:')
        self.addWidgetToForm(self.monthPaymentDay, 1, 1)

        self.fixedPayment = FormCheckbox('Despesa fixa?')
        slot = self.__makeSlot(self.__setDependent)
        self.fixedPayment.toggled.connect(slot)
        self.addWidgetToForm(self.fixedPayment, 2, 0)

        self.fixedPaymentDate = FormInput('Data final pagamento: ')
        self.fixedPaymentDate.setDisabled(True)
        self.addWidgetToForm(self.fixedPaymentDate, 2, 1)

        self.spacement = Spacement(5)
        self.addWidgetToForm(self.spacement, 3, 0)

        self.submitButton = FormButton('Adicionar despesa')
        self.addWidgetToForm(self.submitButton, 4, 0, 1, 2)

    def addWidgetToForm(self, widget: QWidget, *args, **kwargs):
        self.addWidget(widget, *args, **kwargs)

    def __makeSlot(self, func, *args, **kwargs):
        @Slot()
        def slot(checked):
            func(checked, *args, **kwargs)
        return slot

    def __setDependent(self, checked):
        self.fixedPaymentDate.setDisabled(not checked)
        self.fixedPaymentDate.setText('')
