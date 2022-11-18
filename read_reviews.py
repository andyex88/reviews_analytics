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
