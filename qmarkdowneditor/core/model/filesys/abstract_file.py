from pathlib import Path
import os
import shutil as sh


class AbstractFile:
    name: str
    path : str 
    
    def __init__(self, path):
        
        self.setPath(path)
            
    def getName(self):
        return self.name 
        
    def getPath(self):
        return self.path
    
    def setPath(self,path):
        self.path = Path(path)
        self.name = self.path.name
        
    def getAbsPath(self):
        return self.path.absolute().parent
    
    def getParentPart(self):
        return self.path.parent
    
    def rename(self, new_name):
        sh.move(self.path, os.path.join(self.getAbsPath(),new_name))
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        