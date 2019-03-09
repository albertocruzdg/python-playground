import time

def fibonacci (previous, current):
  if current == 0:
    return 1
  return previous + current

previous = 0
current = 0

for i in range(10):
  previous, current = current, fibonacci(previous, current)
  print (current)
  time.sleep(0.5)