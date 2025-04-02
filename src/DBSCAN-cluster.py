filePath = 'Input datafile.txt'
prices = []
try:
	with open(filePath) as f:
		for x in f.readlines():
			prices.append(float(x.strip('')))
except Exception as ex:
	print(ex)
	f.close()
print(len(prices))