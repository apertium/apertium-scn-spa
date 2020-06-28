import sys

f = open(sys.argv[1]).readlines()

eng_list = []
ita_list = []

new_ita_list = []
both_list = []

for line in f:
	line = line.strip().split('\t')
	scn_word = line[0].strip()
	spa_word = line[2].strip()
	from_lang = line[3].strip()
	freq = line[4].strip()

	if(from_lang == 'from-ITA'):
		ita_list.append([[scn_word, spa_word], freq])

	elif(from_lang == 'from-ENG'):
		eng_list.append([[scn_word, spa_word], freq])

	else:
		print(line)

for i in ita_list:
	pair = i[0]
	freq = i[1]

	flag = 0
	for j in eng_list:
		if pair == j[0]:
			flag = 1
			break

	if(flag == 1):
		weight = float(freq)
		both_list.append([pair[0], pair[1], str(weight)])
	else:
		weight = float(2*float(freq))
		new_ita_list.append([pair[0], pair[1], str(weight)])


print("FROM BOTH ITA AND ENG:\n")

for i in both_list:
	print(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + 'from-ITA-and-ENG')

print("\n\n****\n\nFROM ONLY ITA:\n")

for i in new_ita_list:
	print(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + 'from-ITA')







