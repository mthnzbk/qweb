from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QUrl, pyqtSignal
from .lineedit import LineEdit
from .webview import WebView


class Tab(QWidget):

    newTabRequest = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        addressline_layout = QHBoxLayout()
        self.layout().addLayout(addressline_layout)


        self.webview = WebView(self)
        self.load(QUrl("http://google.com"))
        self.layout().addWidget(self.webview)

        self.toolbar = QToolBar()
        addressline_layout.addWidget(self.toolbar)

        self.back_buton = self.webview.page().action(QWebEnginePage.Back)
        self.toolbar.addAction(self.back_buton)
        self.forward_buton = self.webview.page().action(QWebEnginePage.Forward)
        self.toolbar.addAction(self.forward_buton)
        self.reload_button = self.webview.page().action(QWebEnginePage.Reload)
        self.toolbar.addAction(self.reload_button)

        self.address_line = LineEdit()
        addressline_layout.addWidget(self.address_line)


        self.webview.urlChanged.connect(self.setAddressLine)
        self.webview.titleChanged.connect(self.setWindowTitle)
        self.webview.iconChanged.connect(self.setWindowIcon)
        self.address_line.returnPressed.connect(self.enterPressed)

        self.windowTitleChanged.connect(self.parent.setWindowTitle)
        self.windowTitleChanged.connect(self.tabTitleChange)
        self.windowIconChanged.connect(self.tabIconChange)

    def tabTitleChange(self):
        index = self.parent.indexOf(self)
        self.parent.setTabText(index, self.windowTitle())
        self.parent.setTabIcon(index, self.windowIcon())

    def tabIconChange(self):
        index = self.parent.indexOf(self)
        self.parent.setTabIcon(index, self.windowIcon())

    def setAddressLine(self, qurl):
        self.address_line.setText(qurl.url())
        self.address_line.linkChanged.emit()

    def enterPressed(self):
        if self.address_line.text().startswith("http"):
            self.webview.load(QUrl(self.address_line.text()))

        elif self.address_line.text().startswith("file://"):
            self.webview.load(QUrl(self.address_line.text()))

        else:
            self.webview.load(QUrl("http://"+self.address_line.text()))


    def load(self, qurl):
        self.webview.load(qurl)