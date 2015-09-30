def coprimes_branch1(m,n):
  return (2*m-n, m)

def coprimes_branch2(m,n):
  return (2*m+2, m)

def coprimes_branch3(m,n):
  return (m+2*n, n)

def triple(m,n):
  return [m**2-n**2, 2*m*n, m**2+n**2]

def triplesum(m,n):
  return sum(triple(m,n))

def traverseTree(mn):
  import pdb; pdb.set_trace()
  sum = triplesum(mn[0],mn[1])
  print sum
  while sum <= 1000:
    traverseTree(coprimes_branch1(mn[0],mn[1]))
    traverseTree(coprimes_branch2(mn[0],mn[1]))
    traverseTree(coprimes_branch2(mn[0],mn[1]))

mn = (2,1)
traverseTree(mn)
