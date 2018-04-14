a = []
c = []
while True:
    b = raw_input("Input>>")
    d = b.split(" ")
    pointer = 0
    for i in range(0, len(d)):

      if d[i] == '*':
          c.append(d[i+1])
      elif d[i] == '>':
          pointer -= pointer
      elif d[i] == '<':
          pointer +=  pointer
      elif d[i] == "?":
          c = []
      elif d[i] == '!':
          print(c)

      elif d[i] == '^':
          print(c[pointer])
