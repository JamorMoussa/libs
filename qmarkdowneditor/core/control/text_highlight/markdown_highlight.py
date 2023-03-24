from PyQt5.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt5.QtCore import Qt
import re

class MarkdownHighLight:
    
    def __init__(self, textarea ):
        
        # get text area
        self.textarea = textarea
        
        # format :
        self.format = QTextCharFormat()
        self.cursor = self.textarea.textCursor()
        
    def setCursorPos(self,start=0,end=0):
        self.cursor.setPosition(start)
        self.cursor.setPosition(end, QTextCursor.KeepAnchor)

    def compile(self,reg_exp,*args):
        pattern = re.compile(reg_exp,*args)
        matches = pattern.finditer(self.full_text)
        return matches
    
    def style(self, bold=False, italic = False , font = None, size = None, fd = None):
        if bold:
            self.format.setFontWeight(QFont.Bold)
        else:
            self.format.setFontWeight(QFont.Normal)
        
        self.format.setFontItalic(italic)
        if fd:
            self.format.setForeground(fd)
        if size:
            self.format.setFont(QFont(font,size))
    
        
    def default(self,*args):
        self.cursor.setPosition(0)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.full_text))
        self.style(*args)
        
    def bold(self):
        matches = self.compile(reg_exp = r'_{2}(.*?)_{2}')
        for matche in matches:
            start, end = matche.span()
            self.setCursorPos(start+2,end-2)
            self.style(bold=True)
            self.cursor.mergeCharFormat(self.format)
            #
            
    def italic(self):
        matches = self.compile(r'\*{1}(.*?)\*{1}')
        for matche in matches:
            start, end = matche.span()
            self.setCursorPos(start+1,end-1)
            self.style(italic=True)
            
            
    def textChanged(self):
        
        self.full_text = self.textarea.toPlainText()
        
        # default highlight :
        self.default(False, False ,"Segeo UI",15, Qt.black)
        
        # code highlight
        #self.code_highlight()
        
        # bold highlight :
        self.bold()
        
        # italic effect :
        #self.italic()

'''''
class MarkdownHighlight:
    def __init__(self, text_widget, view):
        self.view = view 
        self.text_widget = text_widget
        self.textarea = self.text_widget.textarea
                
        # format :
        self.format = QTextCharFormat()
        self.cursor = self.textarea.textCursor()
        
    def set_cursorPos(self,start=0,end=0):
        self.cursor.setPosition(start)
        self.cursor.setPosition(end, QTextCursor.KeepAnchor)
        
    def compile(self,reg_exp,*args):
        pattern = re.compile(reg_exp,*args)
        matches = pattern.finditer(self.full_text)
        return matches
        
    def text_Changed(self):
        self.full_text = self.textarea.toPlainText()
        self.default_highlight()
        
        # headings highlight :
        self.headings_highlight()
                
        # bold:
        self.bold()
        
        # italic : 
        self.italic()
        
        # code highlight (python code) :
        self.code_highlight()
            
        self.cursor.mergeCharFormat(self.format)
        
        self.updateHtmlPage()
        
    def updateHtmlPage(self):
        
        self.html = soup('<html><head></head><body></body></htnl>','html.parser')
        self.html.head.append(soup(f'''
        #<link rel="stylesheet" type="text/css" href="{css_path}">,'html.parser'))'''''
'''''
        extensions = ['fenced_code','tables']
        self.text = self.textarea.toPlainText()
        mark_text = md.markdown(self.full_text, extensions = extensions)
        htmt_code = soup(mark_text,'html.parser')
        
        self.html.body.append(htmt_code)
        
        
        self.view.setHtml(self.html.prettify(), QUrl.fromLocalFile(css_dir))
        
    def default_highlight(self):
        self.cursor.setPosition(0)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.full_text))
        self.format.setFont(QFont("Segoe UI", 13))
        self.format.setForeground(Qt.black)
        self.cursor.mergeCharFormat(self.format) 
        
    def code_highlight(self):
 
        matches = self.compile(r'`{3}\s*[\w]\s*?[\w\W]*?`{3}')
             
        for matche in matches:
            start, end = matche.span()
            self.set_cursorPos(start,end)
            self.format.setFont(QFont('Consolas'))
            self.format.setFontWeight(QFont.Bold)
            self.format.setForeground(Qt.darkBlue)
            self.cursor.mergeCharFormat(self.format)
                    
    def heading_highlight(self, i):
        matches = self.compile(r'^#{%d}\s+(.*)$' % i, re.MULTILINE)
        
        for matche in matches:
            start, end = matche.span()
            self.set_cursorPos(start,end)
            self.format.setFont(QFont('Lato',20-2*i))
            self.format.setFontWeight(QFont.Normal)
            self.format.setForeground(Qt.black)
            self.cursor.mergeCharFormat(self.format)
            
    def headings_highlight(self):
        for i in range(1,7):
            self.heading_highlight(i)
            
        
    def bold(self):
        matches = self.compile(r'_{2}(.*?)_{2}')
        for matche in matches:
            start, end = matche.span()
            self.set_cursorPos(start+2,end-2)
            self.format.setFontWeight(QFont.Bold)
            self.format.setForeground(Qt.black)
            self.cursor.mergeCharFormat(self.format)
            

    def italic(self):
        matches = self.compile(r'\*{1}(.*?)\*{1}')
        for matche in matches:
            start, end = matche.span()
            self.set_cursorPos(start+1,end-1)
            self.format.setFontWeight(QFont.Normal)
            self.format.setFontItalic(True)
            self.format.setForeground(Qt.black)
            self.cursor.mergeCharFormat(self.format)
            
            
'''''
            
            
            
            
            
            
