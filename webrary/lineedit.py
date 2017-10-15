from PyQt5.QtWidgets import QLineEdit, QAction, QStyle, QStyleOptionFrame
from PyQt5.QtGui import QIcon, QPainter, QColor, QBrush, QLinearGradient, QGradient
from PyQt5.QtCore import pyqtSignal, Qt, QRect


class LineEdit(QLineEdit):

    linkChanged = pyqtSignal()
    isFirstFocus = False
    progress = 24

    def __init__(self):
        super().__init__()

        self.infoAction = QAction(QIcon("images/about.svg"), "Info")
        self.bookmarkAction = QAction(QIcon("images/star-empty.svg"), "Add Bookmarks")
        #self.addAction(self.infoAction, QLineEdit.LeadingPosition)
        #self.addAction(self.bookmarkAction, QLineEdit.TrailingPosition)



        self.linkChanged.connect(self.cursorToHome)


    def cursorToHome(self):
        self.setCursorPosition(0)

    def focusOutEvent(self, event):
        self.isFirstFocus = False

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if not self.isFirstFocus:
            self.cursorToHome()
            self.selectAll()

        else:
            self.deselect()
        self.isFirstFocus = True

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.transparent)
        painter.setBrush(Qt.transparent)

        linGrad = QLinearGradient(0, 0, self.width(), self.height())
        linGrad.setColorAt(0, Qt.red)
        linGrad.setColorAt(0.5, Qt.yellow)
        linGrad.setColorAt(1, Qt.green)
        linGrad.setSpread(QGradient.PadSpread)
        painter.setBrush(linGrad)
        painter.drawRect(0, 0, self.width(), self.height())

