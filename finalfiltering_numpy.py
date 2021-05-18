#Our final function, coin_flip_filter will apply a filter using a boolean array as the condition. We'll first create a boolean coin flip array with the same shape as data.
#Then we filter data using bool_coin_flips as the condition. For the False values in bool_coin_flips, we replace the corresponding index in data with a 1.
def coin_flip_filter(data):
  coin_flips = np.random.randint(2, size=data.shape)
  bool_coin_flips = coin_flips.astype(np.bool)
  one_replace = np.where(bool_coin_flips, data, 1)
  return one_replace
