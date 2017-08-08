import csv
countCount = {}
altNames = {}
with open('realCountryCodes.csv','r',encoding='utf8') as allList:
	reader = csv.reader(allList)
	for row in reader:
		lowered = row[0].lower()
		countCount[lowered] = 0
		altNames[row[1].lower()] = lowered
		altNames[row[2].lower()] = lowered
with open('usStates.csv','r',encoding='utf-8') as states:
	r = csv.reader(states)
	for state in r:
		altNames[state[0].lower()] = 'united states'
		altNames[state[1].lower()] = 'united states'
altNames['england'] = 'united kingdom'
altNames['united states of america'] = 'united states'
altNames["people's republic of china"] = 'china'
fw = open('countryNums.csv','w',encoding='utf-8')
with open('affilsOnly5.csv','r',encoding='utf-8') as affils:
	reader = csv.reader(affils)
	i = 0
	for affil in reader:
		country = (affil[0].split(',')[-1][1:-1]).lower()
		try:
			if country in countCount:
				countCount[country] += int(affil[3])
			elif altNames[country] in countCount:
				countCount[altNames[country]] += int(affil[3])
		except KeyError:
			for country,num in countCount.items():
				if affil[0].lower().find(country) != -1:
					countCount[country] += int(affil[3])
					break
			else:
				i += 1
	print(str(i))
for country,num in countCount.items():
	fw.write(country+','+str(num)+'\n')