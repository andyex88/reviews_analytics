data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))

print('This file has', len(data), 'data sets')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('The average length of comments is', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('We have', len(new), 'reviews that have less than 100 words')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('It have', len(good), 'reviews that have mentioned \'good\'')
print(good[0])


#print(data[0])

# Word counting function 
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # add new key to wc dictionary

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Andy'])

while True:
	word = input('Please enter the word you want to search: ')
	if word == 'q':
		break
	if word in wc:
		print(word, 'shows', wc[word], 'times')
	else:
		print('No such word!')

print('Thanks for using this tool!')

