import functools

def counter(fun):
	counter.nc = 0
	counter.rd = 0
	counter.mrd = 0
	@functools.wraps(fun)
	def wrapper(*args, **kwargs):
		if counter.rd == 0:
			counter.nc = 0
			counter.rd = 0
			counter.mrd = 0
		counter.nc+=1
		counter.rd+=1
		if counter.rd > counter.mrd:
			counter.mrd = counter.rd
		result = fun(*args, **kwargs)
		counter.rd-=1
		wrapper.ncalls = counter.nc
		wrapper.rdepth = counter.mrd
		return result
	return wrapper

