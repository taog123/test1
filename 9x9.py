#
# for i in range(1,10):
#  for j in range(1,i+1):
#     print("%2dX%d=%2d" % (j,i,i*j),end= '\t')
#  print()
#

# print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for  y in  range(1,x+1)])for  x in range(1,10)]))


for i in range(1,10):
  for j in range(1,i+1):
     print('{}*{}={}'.format (j,i,i*j),end= '\t')
  print()

  # for i in range(9, 0, -1):
  #
  #     for j in range(9, i - 1, -1):
  #         print('{}*{}={}'.format(j, i, i * j), end='\t')
  #     print()
  #
