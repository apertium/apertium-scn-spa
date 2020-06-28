import sys 
import hashlib
import xml.etree.ElementTree as ET
import re

if(sys.argv[1]):
	tree = ET.parse(sys.argv[1])
	root = tree.getroot()

	entries = []
	for p in root.findall('.//e/p'):

		l = p.find('.//l')
		r = p.find('.//r')

		ltags = '.'.join([i.attrib['n'] for i in l.findall('.//s')])
		rtags = '.'.join([i.attrib['n'] for i in r.findall('.//s')])

		bflag = len(l.findall('b')) + len(r.findall('b'))

		if(l.text and r.text):
			if(' ' not in l.text and ' ' not in r.text):
				if(bflag == 0):
					print(l.text + '\t' + ltags + '\t' + r.text + '\t' + rtags)

		#print(e.find('p').find('l').text)
		#print(e.find('p').find('r').text)

	# 	for ls in e.findall('.//l'):
	# 		print(ls)
	# 	left = 
	# 	[ls.attrib['n'] for ls in e.findall('.//l')]
	# 	# Join them into a string, n.m.sg and append to the list
	# 	entries.append('.'.join(rights))
			
	# 	# Unique and sort the list
	# 	entries = list(set(entries))
	# 	entries.sort()
	# 	# Make a hash of the list to make similar paradigms similar
	# 	h = hashlib.md5(':'.join(entries).encode('utf-8')).hexdigest()
	# 	if h not in equivs:
	# 		equivs[h] = []
	# 	equivs[h].append(pardef.attrib['n'])

	# par_hash = {}
	# # Print out equivalence classes
	# for h in equivs:
	# 	print(h, equivs[h])

	# 	for par in equivs[h]:
	# 		par_hash[par] = h
