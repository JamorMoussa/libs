from .core.view import TextWidget, ToolBar
from .core import abs_path
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QVBoxLayout, QWidget
import sys
import os



class QMarkdownEditor(QMainWindow):
    def __init__(self):
        super(QMarkdownEditor, self).__init__()
        
        # proprieties :
        self.resize(700,500)
        self.mainwidget = QWidget(self)
        self.setCentralWidget(self.mainwidget)
        self.mainlayout = QVBoxLayout(self)
        self.mainlayout.setContentsMargins(*[0]*4)
        self.mainwidget.setLayout(self.mainlayout)
        
        # text 
        self.text = TextWidget()
        self.mainlayout.addWidget(self.text)
        
        # tool bar :
        self.toolbar = ToolBar()
        self.addToolBar(self.toolbar)
               
        
        with open(f'{abs_path}\\view\\style\\style.qss','r') as f:
            self.setStyleSheet(f.read())    
         


    

    
if __name__ == '__main__':

    app = QApplication([])

    win = App()
    win.show()
    app.exec()