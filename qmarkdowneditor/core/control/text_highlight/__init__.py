from .markdown_highlight import MarkdownHighLight


class TextHighlight:
    
    @staticmethod
    def setMarkdownHighlight(textarea):
        return MarkdownHighLight(textarea)
    