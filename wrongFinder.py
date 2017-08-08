import csv
f1list = list(open('wrongNums.txt','r',encoding='utf-8'))
f2list = list(open('affilsOnly5.csv','r',encoding='utf-8'))
f3write = open('wrongAffils.csv','w',encoding='utf-8')
for i in f1list:
	f3write.write(f2list[int(i[:-1])])