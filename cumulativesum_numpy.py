#The next function to complete is get_cumsum, which returns the cumulative sums for each row of data.
def get_cumsum(data):
  row_cumsum = np.cumsum(data, axis = 1)
  return row_cumsum
