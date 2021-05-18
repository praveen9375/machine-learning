#The next function, slice_data, will return two slices from the input data.
#The first slice will contain all the rows, but will skip the first element in each row. 
#The second slice will contain all the elements of the first three rows except the last two elements.
def slice_data(data):
  slice1 = data[:, 1:]
  slice2 = data[0:3, :-2]
  return slice1, slice2
