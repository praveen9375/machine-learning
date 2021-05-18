# we filter the data array and replace the non-positive elements with the corresponding element from zeros (which will be a 0).
def replace_zeros(data):
  zeros = np.zeros_like(data)
  zeros_replace = np.where(data>0, data, zeros)
  return zeros_replace
