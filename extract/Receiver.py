import logging
import os
import glob

logger = logging.getLogger(__name__)


'''
    A class representing a data receiver.
        This class provides methods for scanning a folder, retrieving file lists and formats, and accessing the receiver's attributes.
    
    Attributes:
        path (str): The path of the receiver.
        filename (str): The filename associated with the receiver.
        format (list): The format associated with the receiver.

    Methods:
        asset_scan(self): Scans the folder at the specified path to check if it exists, is a directory, and is not empty.
        get_file_list(self): Returns a list of files in the receiver's path.
        get_file_format(self, filename_list): Returns a list of file formats associated with the given filenames.
        get_path(self): Returns the path associated with the receiver.
        get_filename(self): Returns the filename associated with the receiver.
        get_format(self): Returns the format associated with the receiver.
        __str__(self): Returns a string representation of the receiver object.
'''
class Receiver:
   
    def __init__(self, path: str, format:list=None,  filename:str=None):
        '''
        Constructor for Class Receiver
        Parameters 
        path : str
        filename : str
        format : str
        '''
    
        self.path = path
        self.filename = filename
        self.format = format
    
    
    def asset_scan(self):
        '''
        Scan folder data source to check if folder is valid/not_emptyand check
        '''
    
        if os.path.exists(self.path) and os.path.isdir(self.path):
            logger.info("Path exists and is a directory")
            #check if files are present
            if len(glob.glob(os.path.join(self.path, '*'))) > 0:
                logger.info("Folder is not empty")
                return True
            logger.info("Folder is empty")
        logger.info("Path does not exist or is not a directory")
        return False
        
    def get_file_list(self):
        '''
        Return a list of files in the receiver's path
        '''
        return glob.glob(os.path.join(self.path, '*'))
    
    def get_file_format(self,filename_list):
        '''
        Return a list of file formats associated with this receiver.
        Parameters
        ----------
        filename_list: list of str
            List of filenames
        Returns
        -------
        list of str
            List of file formats
        '''
        return [filename.split('.')[-1] for filename in filename_list]
    def get_path(self):
        '''
        Return the path associated with this receiver
        '''
        return self.path
    def get_filename(self):        
        '''
        Return the filename associated with this receiver.
        '''
        return self.filename
    def get_format(self):
        '''
        Return the format associated with this receiver.
        '''
        return self.format
    
    
    def __str__(self):
        '''
        IDT to explain it...
        '''
        return f"Receiver({self.path},{self.filename},{self.format})"