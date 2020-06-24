wik_lines = open("wiktionary-parsed.scn-spa.tsv").readlines()

spa_hash = open("spa_lemma_hash.txt").readlines()
scn_hash = open("scn_lemma_hash.txt").readlines()

spa_hash_list = []
for line in spa_hash:
	line = line.strip().split('\t')
	spa_hash_list.append(line)

scn_hash_list = []
for line in scn_hash:
	line = line.strip().split('\t')
	scn_hash_list.append(line)


for line in wik_lines:
	line = line.strip().split('\t')
	scn_word = line[0].strip()
	spa_info = line[2].strip().split(']]')
	spa_word = spa_info[0].split('[[')[1]
	flag_scn = 0
	flag_spa = 0

	extra_spa_info =  spa_info[0].split('[[')[0] + '\t' + ' '.join(spa_info[1:]).strip()

	scn_final = ""
	for scn_w in scn_hash_list:
		if(scn_w[0].strip() == scn_word):
			scn_final = '\t'.join(scn_w)
			flag_scn = 1
			break

	spa_final = ""
	for spa_w in spa_hash_list:
		if(spa_w[0].strip() == spa_word):
			spa_final = '\t'.join(spa_w)
			flag_spa = 1
			break

	if(flag_scn == 1 and flag_spa == 1):
		output_line = scn_final + '\t' + spa_final

		if(extra_spa_info.strip() != ''):
				output_line += '\t' + extra_spa_info
		
		print(output_line)



	
