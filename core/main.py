#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

main.py: Main 

Version: 1.0.0
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

import os
import sys
import time
import readline

# Colors ...
W = '\033[0m'   # white
R = '\033[31m'  # red
O = '\033[33m'  # orange
G = '\033[32m'  # green		
B = '\033[34m'  # blue
C = '\033[36m'  # cyan
RB = '\033[1;31m'
LC = '\033[1;36m' 

VERSION = "2.0.0 @ linux-x86-64"
ASSISTANCE = R+"Type in this command. If you require assistance, type 'help'\n"+W
MODULE_NUMBER = 1

header = C+""" ____   ___  ____  _    _ _   
|  _ \ / _ \|  _ \| | _(_) |_ 
| |_) | | | | |_) | |/ / | __|
|  _ <| |_| |  __/|   <| | |_ 
|_| \_\\___/|_|   |_|\_\_|\__|
""" + W + "\nTool for write exploits for " + G + "Buffer-Overlfow\n\n"+W

middle = LC+"        [" + O + "   ROPkit version" +W+ LC + ":  2.0.0  	]"+ """
	[   Written by: wilt00x 	]
	[   Modules availables: %d	]\n\n
"""%MODULE_NUMBER + ASSISTANCE

R_M = C+"[*]"+W
F_M = RB+"[-]"+W

RR_M = C+"*"+W
RF_M = RB+"*"+W

SHELL = W+"(rkit)"
	
WARN       = F_M+" Unknown command: "
WARN_VAR   = F_M+" Unknown variable: "+W
WARN_INT   = "\n"+R_M+" Interruption: Type 'quit'."
WARN_INT_MODULE = "\n"+R_M+" Interruption: Type 'exit'."

EXPLOIT_FILE = "/tmp/ropkit-session-exploit-directory/exploit-"
EXPLOIT_DIRECTORY = "/tmp/ropkit-session-exploit-directory/"

def help_struct():
	print(W+"\n[Commands]")
	print("----------\n\n")
	print(W+"\n(Informations):")
	print("---------------\n") 
	sys.stdout.write(G+"	[ show modules ]"+W)
	sys.stdout.write("		Show the availables modules\n") 
	sys.stdout.write(G+"	[ show commands ]"+W)         
	sys.stdout.write("		Show the availables commands\n")
	sys.stdout.write(G+"	[ show version ]"+W)             
	sys.stdout.write("		Show the latest version of rkit\n")
	print(W+"\n(Other):")
	print("--------\n") 
	sys.stdout.write(G+"  	[ set ]"+W)                
	sys.stdout.write("	  		Set variable(s)\n")
	sys.stdout.write(G+"	[ quit ]"+W)             
	sys.stdout.write("		Quit the program\n")
	sys.stdout.write(G+"	[ clear ]"+W)             
	sys.stdout.write("		Clear the screen\n\n")


