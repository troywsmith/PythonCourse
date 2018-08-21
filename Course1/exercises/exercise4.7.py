def computegrade(score):
  if score < 0.0:
    return('Error, score is out of the range')
  elif score > 1.0:
    return('Error, score is out of the range')
  elif score >= 0.9:
    return('A')
  elif score >= 0.8:
    return('B')
  elif score >= 0.7:
    return('C')
  elif score >= 0.6:
    return('D')
  elif score < 0.6:
    return('F')

print(computegrade(0.0))
print(computegrade(0.95))
print(computegrade(0.85))
print(computegrade(0.8))
print(computegrade(0.72))
print(computegrade(0.68))
print(computegrade(0.50))
print(computegrade(1.50))
print(computegrade(-0.6))