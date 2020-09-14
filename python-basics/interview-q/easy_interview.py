def majority_element_indexes(lst):
	'''
	>>> majority_element_indexes([1,1,2]) = [0,1]
	>>> majority_element_indexes([1,2]) = []
	>>> majority_element_indexes([]) = []
	'''
	from collections import Counter
	if lst == []:
		return []

	c = Counter(lst)
	# top_elems = sorted(
	# 	c.keys()
	# )
	
	top_count = c.most_common(1)[0][1]  # max(c.values())
	maj_elem = c.most_common(1)[0][0] #max(c.keys())
	if c[maj_elem] <= len(lst) // 2 :
		return []
	return [i for i, elem in enumerate(lst) if elem == maj_elem]