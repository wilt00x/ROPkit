# -*- coding: utf-8 -*-

"""

reset_module.py : Module

Version: 1.0.0
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

from core import *

def reset_module():
	if os.path.isfile(PATH_SET) is not True:
		inc=0
		if os.path.exists(PATH_ADD): 
			print(RESET)
			inc+=1;os.remove(PATH_ADD)
		if inc!=1: print(F_M+" Please, 'set' least only one variable."+W)
	else:
		file = open(PATH_SET, "r")
		file_value = file.read()

		if file_value == "": 
			print WARN_FSET
		else: 
			os.remove(PATH_SET);print(RESET)
			if os.path.exists(PATH_ADD): os.remove(PATH_ADD)
			if os.path.exists(PATH_EXPLOIT): os.remove(PATH_EXPLOIT)

