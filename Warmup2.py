def string_times(str, n):
    return str*n

def front_times(str, n):
    return str[:(3 if len(str)>3 else len(str))]*n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result
def last2(str):
    count = 0
    last2 = str[-2:]
    # Screen out too-short string case
    if len(str) < 2: return 0
    # Check each substring length 2 starting at i
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count += 1
    return count
def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
    return nums[:4].count(9) > 0

def array123(nums):
    # Iterate with length - 2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

def string_match(a, b):
    count = 0
    shorter = min(len(a), len(b))
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count += 1
    return count