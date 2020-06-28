f = open('verbs_not_in_bidix.tsv').readlines()

for line in f:
	template = "<e w=\"{{{w}}}\"><p><l>{{{1}}}<s n=\"vblex\"/></l><r>{{{2}}}<s n=\"vblex\"/></r></p></e>"

	line = line.strip().split('\t')

	scn_word = line[0].strip()
	spa_word = line[1].strip()
	weight = line[2].strip()

	template = template.replace("{{{1}}}", scn_word)
	template = template.replace("{{{2}}}", spa_word)
	template = template.replace("{{{w}}}", weight)

	print(template)


