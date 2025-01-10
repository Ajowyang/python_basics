words = 'launch school tech & talk'.split(" ")
for i in range (len(words)):
	words[i] = words[i][0].upper() + words[i][1:len(words[i])]

print(" ".join(words))
