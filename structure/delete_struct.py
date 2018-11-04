# -*- coding: utf-8 -*-

"""

delete_module.py : Module

Version: 1.0.0
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

from core import *

def delete_module(set_number):
	file = open(PATH_SET, "r+")
	file_value = file.read()
	file_tokenized = file_value.split(":")
	file_lines = file.readlines()

	file.seek(0)
	for i in file_lines: 
		if i != "OVERFLOW": 
			file.write(i)
	file.truncate()
	file.close()