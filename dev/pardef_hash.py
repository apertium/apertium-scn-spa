import sys 
import hashlib
import xml.etree.ElementTree as ET
import re

if(sys.argv[1] == "scn"):
	tree = ET.parse("../../apertium-scn/apertium-scn.scn.dix")
	root = tree.getroot()
	equivs = {}

	# Loop through all the paradigms
	for pardef in root.findall('.//pardef'):
		entries = []
		# Find all the <e> entries
		es = pardef.findall('.//e')
		for e in es:
			# Collect the right sides (tag strings), <s n="n"/><s n="m"/><s n="sg"/>
			rights = [ls.attrib['n'] for ls in e.findall('.//r/s')]
			# Join them into a string, n.m.sg and append to the list
			entries.append('.'.join(rights))
			
		# Unique and sort the list
		entries = list(set(entries))
		entries.sort()
		# Make a hash of the list to make similar paradigms similar
		h = hashlib.md5(':'.join(entries).encode('utf-8')).hexdigest()
		if h not in equivs:
			equivs[h] = []
		equivs[h].append(pardef.attrib['n'])

	par_hash = {}
	# Print out equivalence classes
	for h in equivs:
		print(h, equivs[h])

		for par in equivs[h]:
			par_hash[par] = h

	print("\n\n****\n\n")

	lines = open("wiktionary-parsed.scn-spa.tsv").readlines()

	dixlines = open("../../apertium-scn/apertium-scn.scn.dix").readlines()

	par_set = set(())
	scn_words = []
	for line in lines:
		line = line.strip().split('\t')
		scn_word = line[0].strip()
		scn_words.append(scn_word)
		
	for dixline in dixlines:
		lm = re.findall("lm=\"[^\"]*", dixline)
		
		if(lm):
			current_lemma = lm[0].strip()[4:]
			if(current_lemma in scn_words):
				#print(current_lemma)

				par = re.findall('par n=\"[^\"]*', dixline)
				temp = ""
				for x in par:
					temp = x[7:]

					for s in equivs:
						if(temp in equivs[s]):
							current_lemma = current_lemma.strip()
							if(' ' not in current_lemma):
				
								output_line = current_lemma.strip() + '\t' + temp.strip() + '\t' + par_hash[temp].strip() #scn_lemma->pardef hash map
								par_set.add(output_line)

	#print output set
	for s in par_set:
		print(s)


#SPANISH

if(sys.argv[1] == "spa"):
	tree = ET.parse("../../apertium-spa/apertium-spa.spa.metadix")
	root = tree.getroot()
	equivs_spa = {}

	# Loop through all the paradigms
	for pardef in root.findall('.//pardef'):
		entries = []
		# Find all the <e> entries
		es = pardef.findall('.//e')
		for e in es:
			# Collect the right sides (tag strings), <s n="n"/><s n="m"/><s n="sg"/>
			rights = [ls.attrib['n'] for ls in e.findall('.//r/s')]
			# Join them into a string, n.m.sg and append to the list
			entries.append('.'.join(rights))
			
		# Unique and sort the list
		entries = list(set(entries))
		entries.sort()
		# Make a hash of the list to make similar paradigms similar
		h = hashlib.md5(':'.join(entries).encode('utf-8')).hexdigest()
		if h not in equivs_spa:
			equivs_spa[h] = []
		equivs_spa[h].append(pardef.attrib['n'])

	par_hash_spa = {}
	# Print out equivalence classes
	for h in equivs_spa:
		print(h, equivs_spa[h])	

		for par in equivs_spa[h]:
			par_hash_spa[par] = h

	print("\n\n****\n\n")

	spa_lines = open("wiktionary-parsed.scn-spa.tsv").readlines()

	spa_dixlines = open("../../apertium-spa/apertium-spa.spa.metadix").readlines()

	par_set_spa = set(())
	spa_words = []

	for line in spa_lines:
		line = line.strip().split('\t')
		spa_info = line[2].strip().split(']]')
		spa_word = spa_info[0].split('[[')[1]
		spa_words.append(spa_word)
		#print(scn_word)
	

	for dixline in spa_dixlines:
		lm = re.findall("lm=\"[^\"]*", dixline)
		
		if(lm):
			current_lemma = lm[0].strip()[4:]
			if(current_lemma in spa_words):
				#print(current_lemma)

				par = re.findall('par n=\"[^\"]*', dixline)
				temp = ""
				for x in par:
					temp = x[7:]

					for s in equivs_spa:
						if(temp in equivs_spa[s]):
							current_lemma = current_lemma.strip()
							if(' ' not in current_lemma):
				
								output_line = current_lemma.strip() + '\t' + temp.strip() + '\t' + par_hash_spa[temp].strip() #scn_lemma->pardef hash map
								par_set_spa.add(output_line)

	#print output set
	for s in par_set_spa:
		print(s)
