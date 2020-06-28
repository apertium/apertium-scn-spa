import sys

lines = open(sys.argv[1]).readlines()
langs = []
for line in lines:
	line = line.split('\t')
	scn_word = line[0].split(':')[1].strip()
	part2 = line[1].split("}}:")
	lang = part2[0][-2:]
	if(lang == "es"):
		spa_words = part2[1].strip()
		spa_words = spa_words.replace("{{trad|es|", "[[")

		num_flag = 0
		if("1." in spa_words):
			num_flag = 1	
		
		spa_words = spa_words.split(',')
	
		num_count = 0

		if(num_flag == 1):
			new_spa_words = []

			for word in spa_words:
				if("1." in word):
					num_count = 1
					new_spa_words.append(word)
					continue

				if(num_count == 1):
					if("2." not in word):
						new_spa_words.append("1. " + word)
					else:
						num_count = 2
						new_spa_words.append(word)

				elif(num_count == 2):
					if("3." not in word):
						new_spa_words.append("2. " + word)
					else:
						num_count = 3
						new_spa_words.append(word)

				elif(num_count == 3):
					if("4." not in word):
						new_spa_words.append("3. " + word)
					else:
						num_count = 4
						new_spa_words.append(word)

				elif(num_count == 4):
					new_spa_words.append("4. " + word)

			spa_words = new_spa_words
		
		for word in spa_words:
			if("[[" in word and ("]]" in word or "}}" in word)):
				if(word != "[[]]"):
					if("[[" in word and "}}" in word):
						temp = word.split(' ')
						new_temp = []
						for x in temp:
							x = x.strip()
							if("[[" in x and "}}" in x):
								new_temp.append(x.replace("}}", "]]"))
							else:
								new_temp.append(x)

						temp = ' '.join(new_temp)

						print(scn_word, "\t", "::", "\t", temp.strip())
					else:
						print(scn_word, "\t", "::", "\t", word.strip())



