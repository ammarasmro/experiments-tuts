def multipliers():
  return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]

def multipliers():
  for i in range(4): yield lambda x : i * x 

print [m(2) for m in multipliers()]

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

print [m(2) for m in multipliers()]

def multipliers(x):
    lst = []
    for i in range(4):
        lst.append(i*x)
    return lst

print multipliers(2)