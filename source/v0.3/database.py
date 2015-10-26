import os
import urllib.request
from const import Const
from bmm_parser import Parser
from dirCreator import DirCreator



class Database():

    def local():
        # walk the downloads dir
        # build the local database
        gdldir = Const.gdldir()
        DirCreator.dirExistCheck(gdldir)
        dirs = os.listdir(gdldir)
        localdb = []
        i = 0
        for d in dirs:
            fpath = gdldir + d
            try:
                files = os.listdir(fpath)
            except:
                files = []
            for f in files:
                localdb = Parser.parse_lcldb(localdb, d, f, i)
                i += 1
        return (localdb)

    def build():
        m = ['CATEGORY', 'NAME', 'VERSION', 'DOWNLOADED?', 'INSTALLED?']
        print (m)
        localdb = Database.local()
        mode = ''
        # try connecting to online database
        try:
            onlinedb = urllib.request.urlopen(Const.dburl())
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
                db[i] = db[i].split()
                db[i] = [str(i)] + db[i]
                print (db[i])
                i += 1
            mode = 'online'

        # if connection fails, use local database
        except:
            db = localdb
            for i in range(len(db)):
                db[i] = db[i].split()
                db[i] = [str(i)] + db[i]
                db[i].insert(4, 'downloaded')
                print (db[i])
            mode = 'offline'
                
        return (db, mode)
