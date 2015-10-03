def coprimes_branch1(m,n):
  print 'branch1'
  return (2*m-n, m)

def coprimes_branch2(m,n):
  print 'branch2'
  return (2*m+n, m)

def coprimes_branch3(m,n):
  print 'branch3'
  return (m+2*n, n)

def triple(m,n,k):
  return [k*(m**2-n**2), k*(2*m*n), k*(m**2+n**2)]

def triplesum(m,n,k):
  return sum(triple(m,n,k))

def traverseTree(mn):
  sum = 0
  k = 1
  while sum < 1000:
    sum = triplesum(mn[0],mn[1],k)
    k += 1
    if sum == 1000:
      print mn
      print k
      print triple(mn[0],mn[1],k)

  
  sum = triplesum(mn[0],mn[1],1)
  if sum <= 2000:
    traverseTree(coprimes_branch1(mn[0],mn[1]))
    traverseTree(coprimes_branch2(mn[0],mn[1]))
    traverseTree(coprimes_branch3(mn[0],mn[1]))

mn = (3,1)
traverseTree(mn)
# sum = 1000
# for a in range(1,sum/3):
#   for b in range(1,sum/2):
#     c = sum - a - b
#     if (a**2 + b**2 == c**2):
#       print a*b*c