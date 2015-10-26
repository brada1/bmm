import os

class Const():

    def cd():
        return (os.getcwd() + '\\Besiege_Data\\')

    def url():
        return ('https://github.com/brada1/bmm/raw/master/downloads/')

    def dburl():
        return(Const.url() + 'onlinedb.txt')
    
    def gdldir():
        return(Const.cd() + 'Downloads\\')
    
    def instldir():
        return(Const.cd() + 'Mods\\')
    
    def unity_script():
        return(Const.cd() + 'Managed\\Assembly-UnityScript.dll')
