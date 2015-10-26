BESIEGE MOD MANAGER v0.3(Besiege v0.20)

Still in development - use for testing only!

![Screenshot](https://github.com/brada1/bmm/raw/master/screenshot.jpg)

INSTALLATION:

- Uninstall Spaar's mod loader (you can leave it installed, but then do not install through the manager)
- Make a backup of your mods directory and delete the original (the loader can't figure out what is pre-installed there yet) 
- Download [bmm0.3.exe](https://github.com/brada1/bmm/raw/master/source/builds/bmm0.3.exe) into your Besiege dir (where Besiege.exe is)


USAGE:

Run bmm0.3.exe and have fun.


CHANGELOG (v0.3):

- introduced GUI

- made the Parser class more consistent

- updated database for Besiege v0.20 mods

- now there is an offline and an online mode of the manager (automatic)


TO DO LIST:

- clean up the BMMgui class
	- do et man

- optimize database comparison algorithm

- fill in database

- ultimately, migrate database to a dedicated server (co-op with other modders)

- inclide versioning of mods

- include custom .lvl management

- work closely with the modLoader.json file to allow enabling/disabling a mod instead of installing/uninstalling


TECHNICAL INFO:

![Besiege Mod Manager Class Structure](https://github.com/brada1/bmm/raw/master/source/v0.3/bmm_class_structure.jpg)

- BMMgui():
	- asks the user for operations on downloading/removing and installing/uninstalling mods
	- calls the Database() class to show a list of mods
	- calls the Installer(), Downloader() if the user wishes to
	- does not remove downloaded .zip files so that they are available for installation in offline mode
- Database():
	- scans the downloads dir and creates a local database
		- this contains info about which mods are downloaded, their version and if they are installed or not
	- connects to the online database to get a list of all the availabe mods for download
		- also checks the newest version and where it should be downloaded locally
	- compares the local and online databases to see what's up
	- calls the Parser() and the Const() classes to get the local paths
	- calls DirCreator() if the downloads dir doesn't exist
- Downloader():
	- downloads or removes a downloaded .zip of a mod
	- calls the Parser() class to get the necessary paths and urls
	- calls DirCreator() if a particular subdir of the downloads dir doesn't exist
- Installer():
	- installs or deinstalls a given mod
	- has a special case for Spaar's Mod Loader
	- calls the Parser() and the Const() classes to get the required paths and urls
- Parser():
	- does the heavy lifting of parsing paths and urls
- DirCreator():
	- creates a dir if it doesn't exist
- Const():
	- contains some constants and variables 

BUILD TOOLS:
- Python v3.4.3
- wxPython Phoenix v3.0.3.dev1830+0b5f910 (unofficial release)
- py2exe v 0.9.2.2
