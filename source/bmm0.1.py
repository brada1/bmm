import urllib.request
import os
from installer import Installer
from downloader import Downloader
from bmm_parser import Parser

instr = ''
while instr != 'exit':

    # walk the download dir
    dlds = Parser.get('dlds')
    dirs = os.listdir(dlds)
    offlinedb = []
    i = 0
    for d in dirs:
        fpath = dlds + '\\' + d
        files = os.listdir(fpath)
        for f in files:
            f = f.split('-')
            offlinedb.append(d + ' ' + f[0] + ' ' + f[1][:-4])
            if 'installed_' in offlinedb[i]:
                offlinedb[i].replace('installed_', '')
                offlinedb[i] = offlinedb[i] + ' installed'
            i += 1

    # connect to online database and print it out
    dbheaders = 'ID CATEGORY NAME VERSION DOWNLOADED? INSTALLED?'
    print (dbheaders)
    ondb = urllib.request.urlopen(Parser.get('dburl'))
    i = 0
    onlinedb = []
    for line in ondb:
        line = str(line)
        e = line.find('\\')
        onlinedb.append(line[2:e])
        if onlinedb[i] in offlinedb:
            print (str(i) + ' ' + onlinedb[i] + ' downloaded')
        elif onlinedb[i] or onlinedb[i] + ' installed' in offlinedb:
            print (str(i) + ' ' + onlinedb[i] + ' downloaded installed')
        else:
            print (str(i) + ' ' + onlinedb[i])
        i += 1

    instr = input("enter mod id and instruction(s). e.g.: '2 download install'\n")
    if instr != 'exit':
        inp = int(instr.split(' ')[0])
        parsed = Parser.parse(onlinedb[inp])
        if 'download' in instr:
            Downloader.dl(parsed[0], parsed[1])
            if 'install' in instr:
                Installer.install(parsed[2], parsed[3])
        elif 'uninstall' in instr:
            Installer.uninstall(parsed[2], parsed[3])
            if 'remove' in instr:
                Downloader.rm(parsed[0], parsed[1])
    elif instr == 'exit':
        print ('exiting...')
        break
            



    

    

