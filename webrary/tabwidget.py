from PyQt5.QtWidgets import QTabWidget, QPushButton, QTabBar
from PyQt5.QtCore import QUrl, Qt
from .tabbar import TabBar
from .tab import Tab

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setTabBar(TabBar())


        self.addTab(Tab(self), "about:blank")
        p = QPushButton("a")
        #p.setFixedSize(15, 15)
        #self.tabBar().setTabButton(0, QTabBar.RightSide, p)

        self.setCornerWidget(p, Qt.TopRightCorner)


        self.windowTitleChanged.connect(self.parent.setWindowTitle)
        self.currentChanged.connect(self.windowTitleChange)
        self.tabBar().tabCloseRequested.connect(self.tabClose)

    def newTab(self, qurl=QUrl("about:blank")):
        tab = Tab(self)
        tab.load(qurl)
        index = self.addTab(tab, "about:blank")
        self.setCurrentIndex(index)

    def tabClose(self, index=None):
        if index is None:
            index = self.currentIndex()

        if self.tabBar().count() > 1:
            self.removeTab(index)

        else:
            widget = Tab(self)
            widget.load(QUrl("about:blank"))
            self.addTab(widget, "about:blank")
            self.removeTab(index)

    def windowTitleChange(self, index):
        widget = self.widget(index)
        self.setWindowTitle(widget.windowTitle())