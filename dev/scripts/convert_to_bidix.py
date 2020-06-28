import re

lines = open("wiktionary-parsed.scn-spa.tsv").readlines()

dixlines = open("../../apertium-scn/apertium-scn.scn.dix").readlines()

par_set = set(())
for line in lines:
	line = line.strip().split('\t')
	scn_word = line[0].strip()
	
	for dixline in dixlines:
		if scn_word in dixline:
			par = re.findall('par n=\"[^\"]*', dixline)
			temp = ""
			for x in par:
				temp += x + '\t'
			
			print(temp)
			par_set.add(temp)


print(par_set)


