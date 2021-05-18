# we'll complete col_min, which returns the minimums across each column of data.
def col_min(data):
  min0 = data.min(axis = 0)
  return min0
