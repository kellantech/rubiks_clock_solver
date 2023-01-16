"""
edges/center:
  0 
3 4 1
  2
corners:
0  1

3  2

"""
## enter state here
ef = [0,0,0,0,0] # front edges/center
eb =[0,0,0,0,0] # back edges/center
c =  [0,0,0,0] # corners (as veiwed from the front)
##

m1 = ((eb[0]-eb[1]) + (eb[2]- eb[3]))%12

m2 = (eb[3]-eb[2])%12

m3 = (eb[4]-eb[0])%12

m4 = (eb[4]-eb[3])%12

m5 = (eb[1]-m4)%12
urm = (ef[2]-ef[4])%12
print(f"UR ({urm},{m5})")

ef[0] += urm
ef[1] += urm
c[1] += urm

c[0] += m5
c[2] += m5
c[3]+=m5


drm = (ef[3]-ef[2])%12
print(f"DR ({ef[3]-ef[2]},0)")
ef[1] += drm
ef[2] += drm

c[2] += drm

dlm = (ef[0]-ef[3])%12
print(f"DL ({dlm},0)")

ef[2] += dlm
ef[3] += dlm
c[3] += dlm
lm = (ef[1]-ef[0])%12
print(f"L ({lm},{m1})")
ef[0] += lm
ef[2] += lm
ef[3] += lm
c[0] += lm
c[3] += lm
c[1] += m1
c[2] += m1




cm1 = ((c[1]+m2)-ef[0])%12
print(f"(UR) ({cm1},{m2})")
ef[0] += cm1
c[0] += cm1
c[2] += cm1
c[3]+=cm1

cm2 = ((c[2]+m3)-ef[0])%12
print(f"(DR) ({cm2},{m3})")
ef[0] += cm2
c[0] += cm2
c[1] += cm2
c[3]+=cm2

cm3= ((c[0]+m4)-ef[0])%12
print(f"(UL) ({cm3},{m4})")
ef[0] += cm3
c[1] += cm3
c[2] += cm3
c[3]+=cm3


cm4 = ((c[3])-ef[0])%12
print(f"(DL) ({cm4},0)")
ef[0] += cm4

print(f"ALL {(0-ef[0])%12}")
