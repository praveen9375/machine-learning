def save_points(save_file):
  points = np.random.uniform(low =-2.5, high =2.5, size=(100,2))
  np.save(save_file, points)
