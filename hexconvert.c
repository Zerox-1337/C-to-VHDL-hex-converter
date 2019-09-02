import sys
val = input('Enter a hex num: ')

if len(val) % 2 != 0:
  print("Enter an even number of hex digits")
  sys.exit(1)

def swap(n):
  s = 0
  for i in range(8):
    s |= (n & 1) << (7-i)
    n >>= 1
  return s

out = ''
for i in range(0, len(val), 2):
  a = int(''.join([val[i], val[i+1]]), 16)
  out += '{:02x}'.format(swap(a))


print('Input with padding: ', out)
