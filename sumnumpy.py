#The first function to complete is get_sums, which returns the overall sum and column sums of data.
def get_sums(data):
  total_sum = np.sum(data)
  col_sum = np.sum(data, axis = 0)
  return total_sum, col_sum
