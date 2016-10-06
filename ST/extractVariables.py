import os
import re
import os.path
keywords = [
'auto', 'const', 'double', 'float', 'int', 'short', 'struct', 'unsigned', 'string',
'break', 'continue', 'else', 'for', 'long', 'signed', 'switch', 'void', 'case', 'default', 'enum', 'goto', 'register', 'sizeof', 'typedef',
'volatile', 'char', 'do', 'extern', 'if', 'return', 'static', 'union', 'while', 'asm', 'dynamic_cast', 'namespace', 'reinterpret_cast', 'try',
'bool', 'explicit', 'new', 'static_cast', 'typeid', 'catch', 'false', 'operator', 'template', 'typename', 'class', 'friend', 'private', 'this', 'using',
'const_cast', 'inline', 'public', 'throw', 'virtual', 'delete', 'mutable', 'protected', 'true', 'wchar_t', 'and', 'bitand', 'compl', 'not_eq',
'or_eq', 'xor_eq', 'and_eq', 'bitor', 'not', 'or', 'xor', 'if', 'elif', 'else', 'endif', 'defined', 'ifdef', 'ifndef', 'define', 'undef','include', 'line', 'error', 'pragma']
for pName in os.listdir("sortedPrograms"):
	for program in os.listdir(os.path.join("sortedPrograms", pName)):
		f = open(os.path.join(os.path.join("sortedPrograms", pName), program), "r")
		for content in f.readlines():
			vars = list(set([ x for x in re.findall("[_A-Za-z][_\w]*", content) if x not in keywords]))
			print(vars,pName)
			
			camelCase = 0
			under_score = 0
			caps = 0
			small = 0
			single = 0
			for v in vars:
				if(v):
					if(re.match('([a-z]+[A-Z])+',v)):
						camelCase+=1
					elif(re.match('([a-z]+_[a-z]+)+',v) or re.match('([A-Z]+_[A-Z]+)+',v)):
						under_score+=1
					elif(re.match('^[A-Z][A-Z]+$',v)):
						caps+=1
					elif(re.match('^[a-z][a-z]+$',v)):
						small+=1
					elif(re.match('^[a-zA-Z]$',v)):
						single+=1

			print("camelCase -",camelCase," | under_score -",under_score," | All caps -",caps," | All small -",small," | Single letter -",single)
			print("---------------------------------------------------------------------------------")

		f.close()