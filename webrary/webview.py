from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl


class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        print("ertert")

    def acceptNavigationRequest(self, url, type, isMainFrame):
        super().acceptNavigationRequest(url, type, isMainFrame)
        print("qwe")


class WebView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setPage(WebPage(self))
        source = self.pageAction(QWebEnginePage.ViewSource)
        source.setText("Kaynağı Görüntüle")
        source.setShortcut("Ctrl+U")


    def createWindow(self, type):
        if type == QWebEnginePage.WebBrowserBackgroundTab:
            self.parent.newTabRequest.emit()