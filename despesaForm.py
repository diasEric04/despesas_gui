from PySide6.QtWidgets import QGridLayout, QWidget


class DespesaForm(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def addWidgetToForm(self, widget: QWidget, *args, **kwargs):
        self.addWidget(widget, *args, **kwargs)
