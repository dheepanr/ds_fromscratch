import math

def vector_add(v,w):
	''' adds corresponding elements'''
	return [v_i + w_i for 
	v_i,w_i in zip(v,w)
	]

def vector_subtract(v,w):
	''' substracts corresponding elements'''
	return [v_i - w_i for 
	v_i,w_i in zip(v,w)
	]

def vector_sum(vectors):
	'''takes vectors and applies vector_add function, and reduces'''
	return reduce(vector_add, vectors)

def scalar_multiply(c,v):
	'''c is a number, v is a vector'''
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	'''compute the vector whose ith element is the mean of the ith elements of the input vectors'''
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
	'''dot product, v_1 * w_1 + v_2 * w_2'''
	return sum(v_i * w_i 
		for v_i, w_i in zip(v,w))

def sum_of_squares(v):
	'''sum of squared vector'''
	return dot(v,v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def distance(v,w):
	return magnitude(vector_subtract(v,w))