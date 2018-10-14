

def sleep_in(weekday, vacation):
 return not weekday or vacation


def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

def near_hundred(n):
  return ((abs(n-100) <= 10 ) or (abs(n-200) <= 10))

def missing_char(str, n):
  return str[:n] + str[n+1:]

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))


def pos_neg(a, b, negative):
  return (a < 0) ^ (b < 0) if not negative else (a < 0) and (b < 0)
  

    
    def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]



def sum_double(a, b):
 
  sum = a + b
  
 
  if a == b:
    sum = sum * 2
  return sum

def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

def not_string(str):
  return str if str[:3] == "not" else "not " + str

def front3(str):
 
 return str[:(3 if len(str)>3 else len(str))]*3





