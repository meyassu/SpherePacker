import numpy as np

# multidimensional numpy arrays
# numpy array parameters
	# (.ndim) the dimension of the array
	# (.shape) the shape of a numpy array is (planes/samples,rows,cols)
	# (.size) total number of elements
	# (.dtype) the data type of the elements
	# (.itemsize) byte size of elemens
# automatic array creation functions: 
	# zeros((shape_tuple))
	# ones((shape_tuple))
	# full((shape_tuple),const)
	# eye(num_rows) creates a num_rows x num_rows identity matrix
	# random.random((shape_tuple))

# 2-dimensions
p_a1 = [1,2,3];
p_a2 = [4,5,6];
# accepts as input a single array whose elements are python arrays
# which are basically stacked vertically
n_a = np.array([p_a1,p_a2]);
print(n_a);

# practice: create a rank 2 array with shape (3,4) Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
n_e1 = np.zeros((3,4));
n_e1_sliced = n_e1[:2,1:3];
print(n_e1_sliced);



