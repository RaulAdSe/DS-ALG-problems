from jutge import read

n = read(int)
while n is not None:
  v = [read(float) for i in range(0, n)]
  insertion_sort(v)
  for x in v: print(" {0:.4f}".format(x), end = '')
  print()
  n = read(int)

