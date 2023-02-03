"""
edges/center:
  0 
3 4 1
  2
corners:
0  1

3  2

"""
ef = [0,0,0,0,0]
eb =[0,0,0,0,0]
c =  [0,0,0,0]

ef[0] = int(input("U edge on front face: "))
ef[1] = int(input("R edge on front face: "))
ef[2] = int(input("D edge on front face: "))
ef[3] = int(input("L edge on front face: "))
ef[4] = int(input("center on front face: "))

c[0] = int(input("UL corner on front face: "))
c[1] = int(input("UR corner on front face: "))
c[2] = int(input("DR corner on front face: "))
c[3] = int(input("DL corner on front face: "))


eb[0] = int(input("U edge on back face: "))
eb[1] = int(input("R edge on back face: "))
eb[2] = int(input("D edge on back face: "))
eb[3] = int(input("L edge on back face: "))
eb[4] = int(input("center on back face: "))
def solve(ef,eb,c,SOLVED=0):
  solvlen= 0
  m1 = ((eb[0]-eb[1]) + (eb[2]- eb[3]))%12
  
  m2 = (eb[3]-eb[2]) %12
  
  m3 = (eb[4]-eb[0])%12
  
  m4 = (eb[4]-eb[3])%12
  
  m5 = ((eb[1]-m4)+SOLVED)%12
  
  
  urm = (ef[2]-ef[4])%12
  # UR
  if urm!=0:
    solvlen+=1
    print(f"UR u={urm}")
  if m5 !=0:
    solvlen+=1
    print(f"UR d={m5}")
  
  ef[0] += urm
  ef[1] += urm
  c[1] += urm
  
  c[0] += m5
  c[2] += m5
  c[3]+=m5
  
  
  drm = (ef[3]-ef[2])%12
  if drm!=0:
    solvlen+=1
    print(f"DR u={drm}")
  
  ef[1] += drm
  ef[2] += drm
  
  c[2] += drm
  
  dlm = (ef[0]-ef[3])%12
  if dlm!= 0:
    solvlen+=1
    print(f"DL u={dlm}")
  
  ef[2] += dlm
  ef[3] += dlm
  c[3] += dlm
  lm = (ef[1]-ef[0])%12
  if lm!=0:
    solvlen+=1
    print(f"L u={lm}")
  if m1!=0:
    solvlen+=1
    print(f"L d={m1}")
  
  ef[0] += lm
  ef[2] += lm
  ef[3] += lm
  c[0] += lm
  c[3] += lm
  c[1] += m1
  c[2] += m1
  
  
  #t-c
  
  
  cm1 = ((c[1]+m2)-ef[0])%12
  if cm1!=0:
    solvlen+=1
    print(f"(UR) u={cm1}")
  if m2!=0:
    solvlen+=1
    print(f"(UR) d={m2}")
  
  ef[0] += cm1
  c[0] += cm1
  c[2] += cm1
  c[3]+=cm1
  
  cm2 = ((c[2]+m3)-ef[0])%12
  if cm2!=0:
    solvlen+=1
    print(f"(DR) u={cm2}")
  if m3!=0:
    solvlen+=1
    print(f"(DR) d={m3}")
  
  ef[0] += cm2
  c[0] += cm2
  c[1] += cm2
  c[3]+=cm2
  
  cm3= ((c[0]+m4)-ef[0])%12
  if cm3!=0:
    solvlen+=1
    print(f"(UL) u={cm3}")
  if m4!=0:
    solvlen+=1
    print(f"(UL) d={m4}")
  
  ef[0] += cm3
  c[1] += cm3
  c[2] += cm3
  c[3]+=cm3
  
  
  cm4 = ((c[3])-ef[0])%12
  if cm4!=0:
    solvlen+=1
    print(f"(DL) u={cm4}")
  ef[0] += cm4
  if (SOLVED-ef[0])%12 != 0:
    solvlen+=1
    print(f"ALL u={(SOLVED-ef[0])%12}")
  return solvlen
  
solve(ef,eb,c,0)
