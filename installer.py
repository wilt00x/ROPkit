#! /usr/bin/python2.7

"""

installer.py: Installer 

Version: 1.0.0 
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

from os import geteuid, system

C = '\033[36m'  
W = '\033[0m'   
RB = '\033[1;31m'

R_M = C+"[*]"+W
F_M = RB+"[-]"+W

if geteuid() != 0:
	exit(F_M+" Run this program as 'root'.")

else: 
	system("apt-get update && apt-get install python2.7")
	system("git clone https://gitlab.com/wilt00x/ropkit /usr/share/ropkit/ && chmod +x /usr/share/ropkit/ROPkit && ln -s /usr/share/ropkit/ROPkit /usr/bin/rkit && chmod +x /usr/bin/rkit")
	print(R_M+" Installation of ROPkit is finished ! Type rkit for run the program")
