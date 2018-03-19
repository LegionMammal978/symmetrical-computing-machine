while True:
  program = raw_input("RPN>>")
  d = program.split(" ")
  if d[0] == '+':
     print(int(d[1]) + int(d[2]))
  if d[0] == '-':
     print(int(d[1]) - int(d[2]))
  if d[0] == '/':
     print(int(d[1]) / int(d[2]))
  if d[0] == '*':
     print(int(d[1]) * int(d[2]))
  if d[0] == 'println':
     print(d[1])
  
