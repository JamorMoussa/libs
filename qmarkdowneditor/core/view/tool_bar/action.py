from PyQt5.QtWidgets import QAction

class Action(QAction):
    def __init__(self, text='', tool_bar=None):
        super(Action,self).__init__(text, tool_bar)
        
