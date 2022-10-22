A =int(input("Write A integer? "))
B =int(input("Write B integer? "))
for A in range (A,B+1,1):
    print (A)

i=0
for i in range (0,100):
  if i%7==0:
      continue
  else:
    print (i)

    
numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for number in numbers:
    if number>=150:
      break
    elif int(number%5==0):
      print(number) 