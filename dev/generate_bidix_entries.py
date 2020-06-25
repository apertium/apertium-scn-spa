f = open("pruned-bidix-templates.scn-spa.tsv").readlines()

template_dict = {}
for line in f:
	linet = line.split('\t')

	if len(linet)>3:

		fkey = linet[1].strip() + "--" + linet[2].strip()
		#print(fkey)
		template_dict[fkey] = linet[3].strip()

#print(template_dict)

f2 = open("pruned_wiktionary_parsed_with_hash.tsv").readlines()

for line in f2:
	linet = line.strip().split('\t')

	hash_pair = linet[2].strip() + "--" + linet[5].strip()
	word1 = linet[0].strip()
	word2 = linet[3].strip()
	extra_info = ''

	if(len(linet) > 5):
		extra_info = ' '.join(linet[6:]).strip()
		if(extra_info != ''):
			extra_info = "<!-- " + extra_info + " -->"

	if(hash_pair in template_dict):
		final_template = template_dict[hash_pair]
		final_template1 = final_template.replace("{{{1}}}", word1)
		final_template = final_template1.replace("{{{2}}}", word2)
		print(final_template + '\t' + extra_info)
