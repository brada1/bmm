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



# need to parse install path for the Installer class

##have thi in mind:
##http://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string
##Premature optimization
##
##Even though efficiency isn't the primary goal—writing clear code is—here are some initial timings:
##
##$ python -m timeit '"".join(" \t foo \n bar ".split())'
##1000000 loops, best of 3: 1.38 usec per loop
##$ python -m timeit -s 'import re' 're.sub(r"\s+", "", " \t foo \n bar ")'
##100000 loops, best of 3: 15.6 usec per loop
##
##Note the regex is cached, so it's not as slow as you'd imagine. Compiling it beforehand helps some, but would only matter in practice if you call this many times:
##
##$ python -m timeit -s 'import re; e = re.compile(r"\s+")' 'e.sub("", " \t foo \n bar ")'
##100000 loops, best of 3: 7.76 usec per loop
##
##Even though re.sub is 11.3x slower, remember your bottlenecks are assuredly elsewhere. Most programs would not notice the difference between any of these 3 choices.

