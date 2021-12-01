import math
import random
hoopAxcoord1 = random.randrange(-20,20)
hoopAycoord1 = random.randrange(-20,14)
hoopAheight = round(random.uniform(1,6),5)
hoopAxcoord2 = hoopAxcoord1
hoopAycoord2 = hoopAycoord1 + hoopAheight
hoopBxcoord1 = random.randrange(-20,20)
while hoopBxcoord1 == hoopAxcoord1:
  hoopBxcoord1 = random.randrange(-20,14)
hoopBycoord1 = random.randrange(-20,14)
hoopBheight = round(random.uniform(1,6),5)
hoopBxcoord2 = hoopBxcoord1
hoopBycoord2 = hoopBycoord1 + hoopBheight
hoopCxcoord1 = random.randrange(-20,20)
while hoopCxcoord1 == hoopBxcoord1:
  hoopCxcoord1 = random.randrange(1,6)
hoopCycoord1 = random.randrange(-20,14)
hoopCheight = round(random.uniform(1,6),5)
hoopCxcoord2 = hoopCxcoord1
hoopCycoord2 = hoopCycoord1 + hoopCheight
print "Bottom of Hoop A: (", hoopAxcoord1, ",",  hoopAycoord1, ")"
print "Top of Hoop A: (", hoopAxcoord2, ",",  hoopAycoord2, ")"
print "Bottom of Hoop B: (", hoopBxcoord1, ",",  hoopBycoord1, ")"
print "Top of Hoop B: (", hoopBxcoord2, ",",  hoopBycoord2, ")"
print "Bottom of Hoop C: (", hoopCxcoord1, ",",  hoopCycoord1, ")"
print "Top of Hoop C: (", hoopCxcoord2, ",",  hoopCycoord2, ")"
print 
iteration = 0
for count in range(3):
  score = 0 
  form = random.randrange(1,3)
  if form == 1:
    print ("Enter the equation in standard form:")
    a = float(input("a:"))
    b = float(input("b:"))
    c = float(input("c:"))
  hoopAThruPoint = a*hoopAxcoord1**2 + b*hoopAxcoord1 + c
  hoopBThruPoint = a*hoopBxcoord1**2 + b*hoopBxcoord1 + c
  hoopCThruPoint = a*hoopCxcoord1**2 + b*hoopCxcoord1 + c
  if hoopAThruPoint > hoopAycoord1 and hoopAThruPoint < hoopAycoord2:
    score += 1
  if hoopBThruPoint > hoopBycoord1 and hoopBThruPoint < hoopBycoord2:
    score += 1
  if hoopCThruPoint > hoopCycoord1 and hoopCThruPoint < hoopCycoord2:
    score += 1  
  elif form == 2:
    print ("Enter the equation in vertx form:")
    a = float(input("a:"))
    h = float(input("h:"))
    k = float(input("k:"))
    hoopAThruPoint = a*(hoopAxcoord1-h)**2 + k
    hoopBThruPoint = a*(hoopBxcoord1-h)**2 + k
    hoopCThruPoint = a*(hoopCxcoord1-h)**2 + k
    if hoopAThruPoint > hoopAycoord1 and hoopAThruPoint < hoopAycoord2:
      score += 1
    if hoopBThruPoint > hoopBycoord1 and hoopBThruPoint < hoopBycoord2:
      score += 1
    if hoopCThruPoint > hoopCycoord1 and hoopCThruPoint < hoopCycoord2:
      score += 1  
  elif form == 3:
    print ("Enter the equation in factored form:")
    a = float(input("a:"))
    m = float(input("m:"))
    n = float(input("n:"))
    hoopAThruPoint = a*(hoopAxcoord1-m)*(hoopAxcoord1-n)
    hoopBThruPoint = a*(hoopBxcoord1-m)*(hoopBxcoord1-n)
    hoopCThruPoint = a*(hoopCxcoord1-m)*(hoopCxcoord1-n)
    if hoopAThruPoint > hoopAycoord1 and hoopAThruPoint < hoopAycoord2:
      score += 1
    if hoopBThruPoint > hoopBycoord1 and hoopBThruPoint < hoopBycoord2:
      score += 1
    if hoopCThruPoint > hoopCycoord1 and hoopCThruPoint < hoopCycoord2:
      score += 1  
  iteration += 1
  print
  if score == 3:
    print ("You won!")
    break
  else:
    if iteration < 3:
      print("NOPE! Try again!")
    else: 
      print("You lost!")
