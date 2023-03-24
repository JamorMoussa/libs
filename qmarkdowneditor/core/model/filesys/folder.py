from model.filesys import AbstractFile, File
import os
import shutil as sh
from pathlib import Path


class Folder(AbstractFile):
    
    file_list  = []    
    
    def __init__(self, path=''):
        super(Folder, self).__init__(path)
            
    def fileList(self):
        return self.file_list
    
    def makeIt(self):
        if not self.path.exists():
            os.mkdir(self.path)
            
        else:
            raise Exception('This folder already exists')
        
    def add(self,src):
        src = Path(src)
        dest = os.path.join(self.path,src.name)        
        sh.copy(str(src),dest)
            
    def load(self, path):
        self.setPath(path)
    
        if self.path.exists():
            for file_path in self.path.glob('*'):
                self.file_list.append(File(file_path))
                        
        else:
            Exception('Failed to load') 
            
            
            
            
            
            
            
            
            
             