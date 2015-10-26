import os
from const import Const

class Parser():
############################################################    
    def parse_dl(dbq):
        dlurl = Const.url() + dbq[1] + '/' + dbq[2] + '-' + dbq[3] + '.zip'
        dldir = Const.gdldir() + dbq[1] + '\\'
        dlpath = dldir + dlurl.split('/')[-1]
        m = "attempting to download " + dlurl + " to " + dlpath + '...'
        return (dlurl, dldir, dlpath, m)
    
    def parse_rm(dbq):
        dlpath = Const.gdldir() + dbq[1] + '\\' + dbq[2] + '-' + dbq[3] + '.zip'
        m = 'attempting to remove ' + dlpath + '...'
        return (dlpath, m)
############################################################
    def parse_instl(dbq):
        dlpath = Const.gdldir() + dbq[1] + '\\' + dbq[2] + '-' + dbq[3] + '.zip'
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
#============================================================
    def parse_uninstl(dbq):
        dlpath = Const.gdldir() + dbq[1] + '\\' + dbq[5] + '_' + dbq[2] + '-' + dbq[3] + '.zip'
        instldir = Const.instldir()
        untag_dlpath = dlpath.replace('installed_', '')
        return (dlpath, instldir, untag_dlpath)
        
    def parse_uninstl_spaar(dbq):
        us = Const.unity_script()
        us_bkp = '-bkp'.join([us[:-4],us[-4:]])
        jsonf = Const.cd() + 'Mods\\Config\\modLoader.json'
        m1 = 'removing modded Assembly-UnityScript.dll...'
        m2 = 'restoring backup of Assembly-UnityScript.dll...'
        m3 = 'romoving ' + jsonf + '...'
        return (us, us_bkp, jsonf, m1, m2, m3)
#############################################################
    def parse_lcldb(localdb, d, f, i):
        f = f.split('-')
        localdb.append(d + ' ' + f[0] + ' ' + f[1][:-4])
        if 'installed_' in localdb[i]:
            localdb[i] = localdb[i].replace('installed_', '')
            localdb[i] = localdb[i] + ' installed'
        return (localdb)
