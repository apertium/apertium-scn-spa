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
