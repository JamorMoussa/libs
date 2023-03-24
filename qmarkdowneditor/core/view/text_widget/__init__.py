from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter
from ...control import TextAreaControl 
from ...view.preview import ViewPage
from .text_area import TextArea
from PyQt5.QtCore import QUrl


class TextWidget(QWidget):
    def __init__(self):
        super(TextWidget, self).__init__()
        
        
        # add a layout :
        self.main_layout = QHBoxLayout(self)
        self.mainsplitter = QSplitter()
        
        # text area 
        self.textarea = TextArea()
        self.mainsplitter.addWidget(self.textarea)
        
        # text area 
        self.view = ViewPage()
        self.mainsplitter.addWidget(self.view)
        
        # add splitter :
        self.main_layout.addWidget(self.mainsplitter)

        # add control to textarea && view :
        TextAreaControl(self.textarea, self.view)
        
        