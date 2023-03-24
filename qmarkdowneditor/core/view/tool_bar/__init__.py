from PyQt5.QtWidgets import QToolBar, QAction 
from .action import Action

class ToolBar(QToolBar):
    def __init__(self):
        super(ToolBar, self).__init__()
                    
        self.save = Action("Save", self)
        self.addAction(self.save)
        
