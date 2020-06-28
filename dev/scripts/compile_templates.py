file1 = open("../pruned-bidix-templates.scn-spa.tsv").readlines()
file2 = open("dict_bidix_templates.txt").readlines()
file3 = open("new_wiki_bidix_templates.txt").readlines()

templates = set(())

for line in file1:
	if('#' not in line):
		line = line.strip().split('\t')

		if(len(line)>3):
			templates.add('\t'.join(line[1:]).strip())
			#print('\t'.join(line[1:]).strip())

for line in file2:
	if('#' not in line):
		line = line.strip().split('\t')
		if(len(line)>3):
			templates.add('\t'.join(line[1:]).strip())
			#print('\t'.join(line[1:]).strip())

for line in file3:
	if('#' not in line):
		line = line.strip().split('\t')

		if(len(line)>3):
			templates.add('\t'.join(line[1:]).strip())
			#print('\t'.join(line[1:]).strip())

for x in templates:
	print(x.strip())

