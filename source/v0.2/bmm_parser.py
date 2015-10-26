import os
from const import Const

class Parser():
############################################################    
    def parse_dl(dbq):
        dlurl = Const.url() + dbq.replace(' ', '/', 1)
        dlurl = dlurl.replace(' ', '-') + '.zip'
        dldir = Const.gdldir() + dbq[:dbq.find(' ')] + '\\'
        dlpath = dldir + dlurl.split('/')[-1]
        m = "downloading " + dlurl + " to " + dlpath + '...'
        return (dlurl, dldir, dlpath, m)
    
    def parse_rm(dbq):
        dbq = dbq[:-11]
        dbq = dbq.replace(' ', '\\', 1)
        dbq = dbq.replace(' ', '-')
        dlpath = Const.gdldir() + dbq + '.zip'
        m = 'removing ' + dlpath + '...'
        return (dlpath, m)
############################################################
    def parse_instl(dbq):
        dbq = dbq[:-11]
        dbq = dbq.replace(' ', '\\', 1)
        dbq = dbq.replace(' ', '-')
        dlpath = Const.gdldir() + dbq + '.zip'
        instldir = Const.instldir()
        tmparr = dlpath.split('\\')
        tmparr[-1] = 'installed_' + tmparr[-1]
        tag_dlpath = '\\'.join(tmparr)
        m = 'installing ' + dlpath + ' to ' + instldir + '...'
        return (dlpath, instldir, tag_dlpath, m)    
            
    def parse_instl_spaar():
        us = Const.unity_script()
        us_bkp = '-bkp'.join([us[:-4],us[-4:]])
        instldir = Const.instldir()
        us_instlpath = instldir + 'Assembly-UnityScript.dll'
        m1 = 'backing up Assembly-UnityScript.dll...'
        m2 = 'copying the modded dll...'
        return (us, us_bkp, us_instlpath, m1, m2)
#############################################################
    def parse_uninstl(dbq):
        dbq = dbq[:-21]
        dbq = dbq.replace(' ', '\\installed_', 1)
        dbq = dbq.replace(' ', '-')
        dlpath = Const.gdldir() + dbq + '.zip'
        instldir = Const.instldir()
        untag_dlpath = dlpath.replace('installed_', '')
        return (dlpath, instldir, untag_dlpath)
        
    def parse_uninstl_spaar(dbq):
        us = Const.unity_script()
        us_bkp = '-bkp'.join([us[:-4],us[-4:]])
        json = Const.cd + 'Mods\\Config\\modLoader.json'
        m1 = 'removing modded Assembly-UnityScript.dll...'
        m2 = 'restoring backup of Assembly-UnityScript.dll...'
        m3 = 'romoving ' + json + '...'
        return (us, us_bkp, json, m1, m2)
#############################################################
    def parse_localdb(localdb, d, f, i):
        f = f.split('-')
        localdb.append(d + ' ' + f[0] + ' ' + f[1][:-4])
        if 'installed_' in localdb[i]:
            localdb[i] = localdb[i].replace('installed_', '')
            localdb[i] = localdb[i] + ' installed'
        return (localdb)

            
        
