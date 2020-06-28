bidix = open("lt_expand_bidix_verbs.txt").readlines()
wiktionary = open("verbs_toadd.tsv").readlines()

bidix_word_list = set(())

for line in bidix:
	if ":>:" in line:
		line = line.strip().split(":>:")
		bidix_word_list.add(line[0].split("<")[0] + ":::" + line[1].split("<")[0])

	elif ":<:" in line:
		line = line.strip().split(":<:")
		bidix_word_list.add(line[0].split("<")[0] + ":::" + line[1].split("<")[0])

	else:
		line = line.strip().split(":")
		bidix_word_list.add(line[0].split("<")[0] + ":::" + line[1].split("<")[0])

#print(bidix_word_list)

bidix_unique = []
for s in bidix_word_list:
	bidix_unique.append(s.split(":::"))

#print(bidix_unique)

wik_pairs = []
for line in wiktionary:
	line = line.split('\t')
	word_pair = [line[0].split("<")[0], line[2].split("<")[0]]

	#print(word_pair)

	if(word_pair not in bidix_unique):
		print('\t'.join(word_pair).strip() + '\t' + line[3].strip())










