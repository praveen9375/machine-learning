#The final function, argmax_data, will find the index of each row's maximum element in data. 
#Since there are only 2 dimensions in data, we can apply the operation along either axis 1 or -1.
def argmax_data(data):
  argmax_neg1 = np.argmax(data, axis = -1)
  return argmax_neg1 
