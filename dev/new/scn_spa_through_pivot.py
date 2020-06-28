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
dict_scn_eng_ita = []
#print(d[0])
for line in d:
	line = line.strip().split('\t')
	#print(line)
	
	eng_tag = line[1].strip()
	eng_word = line[0].strip() + eng_tag

	ita_tag = line[3].strip()
	ita_word = line[2].strip() + ita_tag

	scn_tag = line[5].strip()
	scn_word = line[4].strip() + scn_tag

	all_tags.add(eng_tag)
	all_tags.add(scn_tag)
	all_tags.add(ita_tag)

	only_tags = ['<n>', '<n.pl>', '<n.f>', '<adv>', '<n.mf>', '<n.f.pl>', '<vblex>', '<>', '<adj>', '<n.m>', '<n.m.pl>']

	if(eng_tag in only_tags and scn_tag in only_tags and ita_tag in only_tags):
		dict_scn_eng_ita.append([scn_word, eng_word, ita_word])

#print(dict_scn_eng_ita)
final_list = []
final_pairs = set(())
count = 0
flag  = 0
for line in dict_scn_eng_ita:
	flag = 0
	scn_word = line[0].strip()
	if(' ' not in scn_word):

		eng_word = line[1].strip()
		if(' ' not in eng_word):
			if(eng_word in eng_spa):
				flag = 1
				#print("SCN: ", scn_word)
				#print("ENG: ", eng_word)
				#print("SPA: ", eng_spa[eng_word])

				for x in eng_spa[eng_word]:
					temp = scn_word.strip() + '\t::\t' + x.strip()
					if temp not in final_pairs:
						final_pairs.add(temp)
						final_list.append(scn_word.strip() + '\t::\t' + x.strip() + '\tfrom-ENG')

		ita_word = line[2].strip()
		if(' ' not in ita_word):
			if(ita_word in ita_spa):
				flag = 1
				#print("SCN: ", scn_word)
				#print("ITA: ", ita_word)
				#print("SPA: ", ita_spa[ita_word])

				for x in ita_spa[ita_word]:
					temp = scn_word.strip() + '\t::\t' + x.strip()
					if temp not in final_pairs:
						final_pairs.add(temp)
						final_list.append(scn_word.strip() + '\t::\t' + x.strip() + '\tfrom-ITA')

	if(flag == 1):
		count += 1

for line in final_list:
	print(line)




