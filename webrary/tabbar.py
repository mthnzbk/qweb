from PyQt5.QtWidgets import QTabBar
from PyQt5.QtCore import Qt, QUrl


class TabBar(QTabBar):
    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)
        self.setDocumentMode(True)
        self.setElideMode(Qt.ElideRight)
        self.setExpanding(False)
        self.setUsesScrollButtons(False)

        #self.setStyleSheet("QTabBar:tab {width:200px; }")