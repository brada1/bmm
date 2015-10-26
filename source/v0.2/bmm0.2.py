from installer import Installer
from downloader import Downloader
from database import Database

def main():
    instr = ''
    while instr != 'exit':

        db = Database.build() 
        instr = input("\ntype mod ID (e.g. '3') or 'exit'\n")
        try:
            if instr != 'exit':
                inp = int(instr)
                dbq = db[inp]
                print ("choose instruction (e.g. '1')")
                if 'installed' in dbq:
                    inp2 = int(input("'0' - uninstall\n'1' - cancel\n"))
                    if inp2 == 0:
                        Installer.uninstall(dbq)
                    elif inp2 == 1:
                        pass
                elif 'downloaded' in dbq:
                    inp2 = int(input("'0' - install\n'1' - remove\n'2' - cancel\n"))
                    if inp2 == 0:
                        Installer.install(dbq)
                    elif inp2 == 1:
                        Downloader.rm(dbq)
                    elif inp2 == 2:
                        pass
                else:
                    inp2 = int(input("'0' - download\n'1' - cancel\n"))
                    if inp2 == 0:                
                        Downloader.dl(dbq)
                    elif inp2 == 1:
                        pass
            elif instr == 'exit':
                print ('exiting...')
                break
        except ValueError:
            print ('valid ID please')
            continue

if __name__ == "__main__":
    main()
