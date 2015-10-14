import os

class Parser():

    def get(instr):
        # this function returns a basic url or path
        cd = os.getcwd() + '\\Besiege_data' # current working dir
        url = 'https://github.com/brada1/bmm/raw/master/downloads/' # genral url
        dburl = url + '/onlinedb.txt' # url to online database
        dlds = cd + '\\Downloads\\' # general downloads directory
        instldir = cd + '\\Mods\\' # general install dir
        unity_script = cd + '\\Managed\\Assembly-UnityScript.dll' # unity engine libraries directory
        
        if instr == 'cd':
            return (cd)
        elif instr == 'url':
            return (url)
        elif instr == 'dburl':
            return (dburl)
        elif instr == 'dlds':
            return (dlds)
        elif instr == 'instldir':
            return (instldir)
        elif instr == 'unity_script':
            return (unity_script)
        
    def parse(dbquery):
    # this function take a database query and parses download url and path
        
        # parse download url
        dlurl = Parser.get('url') + dbquery.replace(' ', '/', 1)
        dlurl = dlurl.replace(' ', '-') + '.zip'

        # parse download directory
        dld = Parser.get('dlds') + dbquery[:dbquery.find(' ')]

        # parse full path of downloaded mod
        dlf = dld + '\\' + dlurl.split('/')[-1]

        # get installpath
        instlpath = Parser.get('instldir')

        return (dlurl, dld, dlf, instlpath)
