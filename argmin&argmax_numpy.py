#The next function, argmin_data, will find minimum indexes in the input data
def argmin_data(data):
  argmax_all = np.argmin(data)
  argmin1 = np.argmin(data, axis=1)
  return argmax_all,argmin1
