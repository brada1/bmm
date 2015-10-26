import os

class DirCreator():
    
    def dirExistCheck(d):
        # create download directory if it doesn't exist
        if  not os.path.isdir(d):
            print (d + " doesn't exist. Creating it...")
            os.makedirs(d)
