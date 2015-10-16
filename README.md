BESIEGE MOD MANAGER

Still in early development - version 0.2. Use for testing only.


INSTALLATION:
Extract these [python files](source/bmm_0.2_source.rar) into your Besiege dir (where Besiege.exe is).

USAGE:
Run bmm0.2.py using your favourite python interpreter. 
Follow the instructions provided.


TECHNICAL INFO:

[Besiege Mod Manager Class Structure](https://raw.githubusercontent.com/brada1/bmm/master/bmm_class_structure.jpg)

- Main():
	- asks the user for operations on downloading/removing and installing/uninstalling mods
	- calls the Database() class to show a list of mods
	- calls the Installer(), Downloader() if the user wishes to
- Database():
	- scans the downloads dir and creates a local database
		- this contains info about which mods are downloaded, their version and if they are installed or not
	- connects to the online database to get a list of all the availabe mods for download
		- also checks the newest version and where it should be downloaded locally
	- calls the Parser() and the Const() classes to get the required paths and urls
- Downloader():
	- downloads or removes the the downloaded zip of a mod
	- calls the Parser() class to get the necessary paths and urls 
- Installer():
	- installs or deinstalls a given mod
	- has a special case for Spaar's Mod Loader
	- calls the Parser() and the Const() classes to get the required paths and urls
- Parser():
	- does the heavy lifting of parsing paths and urls
- Const():
	- contains some constants and variables 


TO DO LIST:

- include exceptions handling for the downloading, removing, installing and unninstalling processes!

- optimize database comparison algorithm

- fill in database

- add more special installation cases for mods such as the Water Mod

- the manager needs to have an online and offline state
	- in online state it can download and install/uninstall mods
	- in offline state it can only install/uninstall mods

- make a GUI

- build a standalone .exe

- inclide the option for updating to newer mod versions

- include custom .lvl management