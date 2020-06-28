import sys

tocheck_entries = open(sys.argv[1]).readlines()
bidix = open('../../apertium-scn-spa.scn-spa.dix').read()

for line in tocheck_entries:
	if(line.split('\t')[0].strip() not in bidix):
		print(line.strip())



