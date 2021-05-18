#The final function to complete is basic_stats, which returns the mean, median, and variance of data.
def basic_stats(data):
  mean = np.mean(data)
  median = np.median(data)
  var = np.var(data)
  return mean, median, var
