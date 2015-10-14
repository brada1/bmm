import os, zipfile, shutil
from bmm_parser import Parser

class Installer():
    def install(source_filename, install_dir):
        # installs a given mod (only in zip format for now)
        zf = zipfile.ZipFile(source_filename)
        print ('installing ' + source_filename + ' to ' + install_dir + '...')
        zf.extractall(install_dir)
        zf.close()

        # include special case for spaars module
        # make backup of Assembly-UnityScript.dll and then copy the dll from zip
        if 'spaar' in source_filename:
            print ('backing up Assembly-UnityScript.dll...')
            # make backup of Assembly-UnityScript.dll
            us = Parser.get('unity_script')
            os.rename(us, '-bkp'.join([us[:-4],us[-4:]]))
            print ('copying the modded dll...')
            shutil.copyfile(install_dir + '\\Assembly-UnityScript.dll', us)   
            
        # tag the downloaded file as installed
        tmparr = source_filename.split('\\')
        tmparr[-1] = 'installed_' + tmparr[-1]
        tagged_source = '\\'.join(tmparr)
        os.rename(source_filename, tagged_source)
        print ('done')
        
    def uninstall(source_filename, dest_dir):
        # uninstalls a given mod (if it was installed from a zip file only)
        # doesn't remove files generated at runtime
        # doesn't remove directories and subdirs
        print ('uninstalling...')
        tmparr = source_filename.split('\\')
        tmparr[-1] = 'installed_' + tmparr[-1]
        tagged_source = '\\'.join(tmparr)
        with zipfile.ZipFile(tagged_source) as zf:
            # look in the downloaded zip to determine the folder structure
            for member in zf.infolist():
                words = member.filename.split('/')
                path = dest_dir
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''): continue
                    path = os.path.join(path, word)
                path = path + '\\' + words[-1]
                if os.path.isfile(path):
                    # if we have a path to a valid file, delete it
                    print ('deleting ' + path)
                    os.remove(path)

        # include special case for spaars mod loader
        # delete the modded Assembly-UnityScript.dll from the Managed dir
        # restore the created backup
        if 'spaar' in source_filename:
            us = Parser.get('unity_script')
            print ('removing modded Assembly-UnityScript.dll...')
            os.remove(us)
            print ('restoring backup of Assembly-UnityScript.dll...')
            usbkp = '-bkp'.join([us[:-4],us[-4:]])
            os.rename(usbkp, us)
        # need to remove the whole Mods dir
        # then untag all the zip files 
            
                    
        # untag the downloaded file
        os.rename(tagged_source, source_filename)
        print ('done')

# to add special cases for mods such as spaars mod loader
# add installation of .dll files which are not in an archive
