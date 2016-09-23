def min_in_list(list):
	assert list
	m = list[0]
	for i in list:
		if i<m:
			m=i
	return m

list = [1,2,3,4]

min = min_in_list(list)
print(min)

def av_in_list(list):
	assert list
	m = 0
	n = 0
	for i in list:
		m=m+i
		n=n+1
	m=m/n
	return m

list = [1,2,3,4]

av = av_in_list(list)
print(av)
