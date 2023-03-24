from ..markdown_to_html import HtmlPage
from ..text_highlight import TextHighlight
from PyQt5.QtCore import QUrl
from ...view.style import css_dir

class TextAreaControl:
    
    def __init__(self, textarea, view):
        
        self.textarea = textarea
        self.view  = view
        
        # event when text changed :
        self.textarea.keyPressed.connect(lambda : self.text_Changed())
        
        # add highligh event :
        self.MarkHighLight = TextHighlight.setMarkdownHighlight(self.textarea)
        
        # HtmlPage  :
        self.html_page = HtmlPage()
        
    def text_Changed(self):
        
        full_text = self.textarea.toPlainText()
        
        self.view.setHtml(self.html_page.toHtml(full_text), QUrl.fromLocalFile(css_dir))
        
        

        
        
    