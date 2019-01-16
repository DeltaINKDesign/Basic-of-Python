def minF(*S):
  d=S[0]
  for i in S:
    if i<d:
      d=i
  return d

print(minF(1,3,42,4,532,643,745,-2,312,53,253))
