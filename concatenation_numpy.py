#The final function, concat_arrays, takes in two 2-D NumPy arrays as input. It returns the column-wise and row-wise concatenations of the input arrays.
def concat_arrays(data1, data2):
  col_concat = np.concatenate([data1, data2])
  row_concat = np.concatenate([data1, data2], axis=1)
  return col_concat, row_concat
