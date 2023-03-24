from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtGui import QTextCursor
from ...view.style import css_path
from bs4 import BeautifulSoup
import markdown as md


class HtmlPage(BeautifulSoup):
    
    html_base = f'''
    <html>
        <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
            </head>
        <body> 
        ksjdksj     
            </body>
    </htnl>
    
    '''
    
    def __init__(self):
        super(HtmlPage, self).__init__(self.html_base, 'html.parser')
        
    def clear(self):
        self.body.clear()
        
    def toHtml(self, text):
        
        self.clear()
        extensions = ['fenced_code','tables']
        mark_text = md.markdown(text, extensions = extensions)
        htmt_code = BeautifulSoup(mark_text,'html.parser')
        self.body.append(htmt_code)
        
        return self.prettify()






