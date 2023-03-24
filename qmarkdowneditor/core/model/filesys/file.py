from .abstract_file import AbstractFile
from pathlib import Path


class File(AbstractFile):

    def __init__(self, path):
        super(File, self).__init__(path)
        
        self.ext = self.path.suffix
    
    
    def __str__(self):
        return f''' File(name = "{self.getName()}", ext = "{self.ext}", path = "{self.getPath()}") '''
        
        
        
        
        
        
        
        
        
        