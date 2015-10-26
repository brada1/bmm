import urllib.request
import os, shutil
from bmm_parser import Parser
from dirCreator import DirCreator

class Downloader():

    def dl(dbq):
        pointer = Parser.parse_dl(dbq)
        dlurl = pointer[0]
        dldir = pointer[1]
        dlpath = pointer [2]
        m = pointer [3]
        DirCreator.dirExistCheck(dldir)
        print (m)
        with urllib.request.urlopen(dlurl) as resp, open(dlpath, 'wb') as file:
            shutil.copyfileobj(resp, file)
        print ('done')

    def rm(dbq):
        pointer = Parser.parse_rm(dbq)
        dlpath = pointer[0]
        m = pointer[1]
        print (m)
        os.remove(dlpath)
        print ('done')

