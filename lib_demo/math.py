import math

def move(x, y, step, angle):
  nx = x + step*math.cos(angle)
  ny = y + step*math.sin(angle)

  return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(math.sqrt(2))
