import os, zipfile, shutil
from bmm_parser import Parser

class Installer():
    def install(dbq):

        pointer = Parser.parse_instl(dbq)
        dlpath = pointer[0]
        instldir = pointer[1]
        tag_dlpath = pointer[2]
        m = pointer[3]
        
        # installs a given mod (only in zip format for now)
        zf = zipfile.ZipFile(dlpath)
        print (m)
        zf.extractall(instldir)
        zf.close()

        # include special case for spaars module
        # make backup of Assembly-UnityScript.dll
        # then copy the dll from zip
        if 'spaar' in dlpath:
            pointer2 = Parser.parse_instl_spaar()
            us = pointer2[0]
            us_bkp = pointer2[1]
            us_instlpath = pointer2[2]
            m1 = pointer2[3]
            m2 = pointer2[4]

            # make backup of Assembly-UnityScript.dll
            print (m1)
            os.rename(us, us_bkp)
            print (m2)
            shutil.copyfile(us_instlpath, us)   
         

        # tag the downloaded file as installed
        os.rename(dlpath, tag_dlpath)
        print ('done')
        
    def uninstall(dbq):
        # uninstalls a given mod (if it was installed from a zip file only)
        # doesn't remove files generated at runtime
        # doesn't remove directories and subdirs
        pointer = Parser.parse_uninstl(dbq)
        dlpath = pointer[0]
        instldir = pointer[1]
        untag_dlpath = pointer[2]

        print ('uninstalling...')
        with zipfile.ZipFile(dlpath) as zf:
            # look in the downloaded zip to determine the folder structure
            for member in zf.infolist():
                words = member.filename.split('/')
                path = instldir
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''): continue
                    path = os.path.join(path, word)
                path = path + '\\' + words[-1]
                if os.path.isfile(path):
                    # if we have a path to a valid file, delete it
                    print ('deleting ' + path + '...')
                    os.remove(path)

        # include special case for spaars mod loader
        # delete the modded Assembly-UnityScript.dll from the Managed dir
        # restore the backup created during installation
        if 'spaar' in dlpath:
            pointer2 = Parser.parse_uninstl_spaar(dbq)
            us = pointer2[0]
            us_bkp = pointer2[1]
            json = pointer2[2]
            m1 = pointer2[3]
            m2 = pointer2[4]
            m3 = pointer2[5]

            print (m1)
            os.remove(us)
            print (m2)
            os.rename(us_bkp, us)
            print (m3)
            try:
                os.remove(json)
            except:
                pass
                    
        # untag the downloaded file
        os.rename(dlpath, untag_dlpath)
        print ('done')
