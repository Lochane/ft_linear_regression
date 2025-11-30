def ft_mean(lst):
	total = 0
	for v in lst: 
		total += v
	return total / len(lst)

def ft_variance(lst):
	m = ft_mean(lst)
	total = 0
	for n in lst:
		total += (n - m) ** 2
	return total / len(lst)

def ft_std_dev(lst):
	return ft_variance(lst) ** 0.5