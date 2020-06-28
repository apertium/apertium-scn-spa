d = open("eng_ita_scn.tsv").readlines()

si = open("spa-ita_bidix.tsv").readlines()

ita_spa = {}
for line in si:
	line = line.strip().split('\t')
	if(len(line) >= 4):
		spa_word = line[0].strip()
		spa_tags = line[1].strip()

		spa_word = spa_word + '<' + spa_tags + '>'

		ita_word = line[2].strip()
		ita_tags = line[3].strip()

		ita_word = ita_word + '<' + ita_tags + '>'
	else:
		spa_word = line[0].strip()
		ita_word = line[2].strip()

	if(ita_word in ita_spa):
		ita_spa[ita_word].append(spa_word)
	else:
		ita_spa[ita_word] = [spa_word]

#print(ita_spa)

es = open("eng-spa_bidix.tsv").readlines()

eng_spa = {}
for line in es:
	line = line.strip().split('\t')
	if(len(line) >= 4):
		eng_word = line[0].strip()
		eng_tags = line[1].strip()

		eng_word = eng_word + '<' + eng_tags + '>'

		spa_word = line[2].strip()
		spa_tags = line[3].strip()

		spa_word = spa_word + '<' + spa_tags + '>'
	else:
		eng_word = line[0].strip()
		spa_word = line[2].strip()

	if(eng_word in eng_spa):

		eng_spa[eng_word].append(spa_word)
	else:
		eng_spa[eng_word] = [spa_word]

#print(eng_spa)
all_tags = set(())
dict_eng_ita_scn = []
#print(d[0])
for line in d:
	line = line.strip().split('\t')
	#print(line)
	eng_word = line[0].strip()
	eng_tag = line[1].strip()

	ita_word = line[2].strip()
	ita_tag = line[3].strip()

	scn_word = line[4].strip()
	scn_tag = line[5].strip()

	all_tags.add(eng_tag)
	all_tags.add(scn_tag)
	all_tags.add(ita_tag)

print(all_tags)

