#The first function to complete is get_positives.
def argmax_data(data):
  argmax_neg1 = np.argmax(data, axis = -1)
  return argmax_neg1 
