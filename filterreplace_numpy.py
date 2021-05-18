#The next function, replace_neg_one, will replace the non-positive elements of data with -1. Rather than creating a separate array, we'll use broadcasting.
def replace_neg_one(data):
  neg_one_replace = np.where(data>0, data, -1)
  return neg_one_replace
