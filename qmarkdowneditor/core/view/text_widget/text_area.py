from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtCore


class TextArea(QTextEdit):
    keyPressed = QtCore.pyqtSignal(int)
    def __init__(self):
        super(TextArea, self).__init__()

        
    def keyPressEvent(self, event):
        self.keyPressed.emit(event.key())
        super().keyPressEvent(event)
        