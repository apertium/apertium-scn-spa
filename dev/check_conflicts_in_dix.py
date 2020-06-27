f = open("verb_bidix_entries.txt").readlines()
f2 = open("../apertium-scn-spa.scn-spa.dix").readlines()

bidix = []
for l in f2:
	if('<e>' in l):
		bidix.append(l.strip())
#print(bidix)
entries = set(())

for line in f:
	line = line.strip()
	if line not in bidix:
		entries.add(line)

for e in entries:
	print(e)
