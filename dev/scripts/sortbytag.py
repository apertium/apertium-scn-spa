f = open('test.txt').readlines()

tags = set(())
for l in f:
	num = l[0:4].strip()
	rest = l[5:].strip()

	p1 = rest.split('>')[0]
	if(len(p1.split('<')) > 1):
		#print(rest)
		tag = p1.split('<')[1].strip()
		tags.add(tag)
		#print(num, tag)

#print(tags)

for x in ['n', 'adj']:
	print("\nSECTION: ", x)
	for l in f:
		if('<'+x+'>' in l):
			print(l.strip())

