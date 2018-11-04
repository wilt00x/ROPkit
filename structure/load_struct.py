# -*- coding: utf-8 -*-

"""

load_module.py : Module

Version: 1.0.0
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

from core import *
import struct 

def load_module():
	global set_option
	if os.path.isfile(PATH_SET) is not True:
		print WARN_LOAD
	else: 
		file = open(PATH_SET, "r")
		file_value = file.read()

		if file_value == "":
			print WARN_FSET
		else: 
			exploit="a"*1
			file_tokenized = file_value.split(":")
			for opt in set_options[2:]:
				for nb, tok in enumerate(file_tokenized[2:]): 
					if tok == opt: 
						if tok == set_options[3]:
							exploit="a"*int(file_tokenized[nb+3])
			inc=0
			if os.path.exists(PATH_ADD):
				inc+=1
				add_file = open(PATH_ADD, "r")
				add_content = add_file.read()

			save_file = open(PATH_EXPLOIT, "a+")
			save_file.write(exploit);
			print(R_M+" Exploit file is loaded at '/tmp/exploit.bkf'")
			if inc == 1:save_file.write(add_content)
