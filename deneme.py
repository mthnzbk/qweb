from PyQt5 import QtCore, QtWidgets, QtGui
import time




class Dialog(QtWidgets.QDialog):
    value = 0.001
    def __init__(self, parent=None):
        QtWidgets.QDialog .__init__(self, parent)
        mainLayout = QtWidgets.QVBoxLayout()

        self.lineedit = QtWidgets.QLineEdit()
        self.setValues()
        mainLayout.addWidget(self.lineedit)
        button = QtWidgets.QPushButton('Calculate')
        button.clicked.connect(self.buttonClicked)
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)

    def setValues(self):
        self.lineedit.setText('progress %s'%self.value)
        palette = self.lineedit.palette()
        QRectF = QtCore.QRectF(self.lineedit.rect())
        gradient = QtGui.QLinearGradient(QRectF.topLeft(), QRectF.topRight())
        gradient.setColorAt(self.value-0.001, QtGui.QColor('#ff0000'))
        gradient.setColorAt(self.value, QtGui.QColor('#ffffff'))
        gradient.setColorAt(self.value+0.001, QtGui.QColor('#00ff00'))
        palette.setBrush(QtGui.QPalette.Base, QtGui.QBrush(gradient))
        self.lineedit.setPalette(palette)

    def buttonClicked(self):
        if self.value >0.9:
            self.value = 0.001
        else:
            self.value=self.value+0.1

        self.setValues()
        time.sleep(0.1)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Dialog()
    window.resize(300, 50)
    window.show()
    app.exec_()