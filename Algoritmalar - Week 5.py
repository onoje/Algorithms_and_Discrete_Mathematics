c = input("Enter a string to compress: ")
d = input("Enter a compressed string to decompress: ")


def compress_string(c):
  a_list = []
  counter = 1
  i = 0
  while i < len(c) - 1:
    if c[i] == c[i+1]:
      counter = counter + 1
      i = i + 1
      
    elif c[i] != c[i+1]:
      a_list.append(c[i] + str(counter))
      counter = 1
      i = i + 1
    else:
      i = i + 1

  a_list.append(c[i] + str(counter))
  return(a_list)

def decompress_string(d):
  i = 0
  a = ""
  while i < len(d):
    a = a + d[i] * int(d[i+ 1])
    i = i + 2
  return(a)
  
print(compress_string(c))
print(decompress_string(d))