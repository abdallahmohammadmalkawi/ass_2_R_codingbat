def make_bricks(small, big, goal):
  resto = goal
  resto -= 5*min(big,goal/5)
  return resto-small <= 

def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum

def lucky_sum(a, b, c):
  sum = 0
  list = [a,b,c,13]
  for n in list[:list.index(13)]:
    sum += n
  return sum

def no_teen_sum(a, b, c):
  def fix_teen(n):
    return n if n not in [13,14,17,18,19] else 0

  return fix_teen(a)+fix_teen(b)+fix_teen(c)

def round_sum(a, b, c):
  def round10(num):
    return (num+5)/10*10

  return round10(a)+round10(b)+round10(c)

def close_far(a, b, c):
   return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))


def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1