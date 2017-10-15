from PyQt5.QtWidgets import QWidget, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from .tabwidget import TabWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kerkenez Browser")
        self.showMaximized()
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0,0,0,0)

        self.tabwidget = TabWidget(self)

        self.layout().addWidget(self.tabwidget)

        shortcut = QShortcut(QKeySequence("Ctrl+T"), self)
        shortcut.activated.connect(self.tabwidget.newTab)

        shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        shortcut.activated.connect(self.tabwidget.tabClose)

    def setWindowTitle(self, title):
        super().setWindowTitle(title + " - " + "Kerkenez Browser")
        #self.setWindowTitle(title + " " + "Kerkenez Browser")