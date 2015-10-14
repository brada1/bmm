Besiege Mod Manager

Still in early development - version 0.1. It's no use if you are not a developer/modder. 

Installation:
Extract these [python files](source/source.rar) into your Besiege dir (where Besiege.exe is).

Usage:
Run bmm0.1.py using your favourite python interpreter. 
You'll see a database of mods and associated ID's
Do operations by typing these commands in shell/bash:
ID COMMAND (COMMAND)

Examples:

0 download
0 download install
3 uninstall
3 uninstall remove

TO DO LIST:

- optimize overall class structure

- make the role of the parser more clear

- include exceptions handling for the downloading, removing, installing and unninstalling processes!

- optimize database comparison algorithm

- fill in database

- the manager needs to have an online and offline state
	- in online state it can download and install/uninstall mods
	- in offline state it can only install/uninstall mods

- make a GUI

- build a standalone .exe

- inclide the option for updating to newer mod versions

- include custom .lvl management

- make the installation of spaar's mod loade nd tygd's block loader obligatory

- expand the special uninstallation of spaar's mod loader to whipe the Mods dir and to untag all downloaded mods

- 