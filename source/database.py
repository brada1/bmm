import os
import urllib.request
from const import Const
from bmm_parser import Parser

class Database():

    def local():
        # walk the downloads dir
        # build the local database
        gdldir = Const.gdldir()
        dirs = os.listdir(gdldir)
        localdb = []
        i = 0
        for d in dirs:
            fpath = gdldir + d
            files = os.listdir(fpath)
            for f in files:
                localdb = Parser.parse_localdb(localdb, d, f, i)
                i += 1
        return (localdb)

    def build():
        # connect to online database
        # 
        print ('\nID CATEGORY NAME VERSION DOWNLOADED? INSTALLED?')
        onlinedb = urllib.request.urlopen(Const.dburl())
        localdb = Database.local()
        i = 0
        db = []
        for line in onlinedb:
            line = str(line)
            e = line.find('\\')
            db.append(line[2:e])
            for j in range(len(localdb)):
                if db[i] == localdb[j]:
                    db[i] += ' downloaded'
                    break
                elif db[i] + ' installed' == localdb[j]:
                    db[i] += ' downloaded installed'
                    break
            print (str(i) + ' ' + db[i])
            i += 1
        return (db)
