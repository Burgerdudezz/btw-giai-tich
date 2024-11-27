import matplotlib.pyplot as plt
from fractions import Fraction
import sympy as sp
x= []
y= []
v= []
a= []
ph=5
fig,axes=plt.subplots(3,1, figsize=(12,7))
xi=float(Fraction(input("Input initial position: ")))
vi=float(Fraction(input("Input initial velocity: ")))
ai=float(Fraction(input("Input acceleration: ")))
t=sp.symbols('t')
choice=int(input("1/ Graphs for equation. 2/ Example"))
match choice:
      case 1:
            for i in range(ph):
                  yi =xi+vi*t+(ai*t**2)/2
                  vf = sp.diff(yi,t)
                  af = sp.diff(vf,t)
                  ti=i
                  yi_val= yi.evalf(subs={t:ti})
                  vf_val= vf.evalf(subs={t:ti})
                  af_val= af.evalf(subs={t:ti})
                  x.append(ti)
                  y.append(yi_val)
                  v.append(vf_val)
                  a.append(af_val)
      case 2:
                  x.extend([0,10,20,25,40,50 ])
                  y.extend([0,500,500,200,300,0])
                  v.extend([0,15,0,-30,-10,0])
                  a.extend([4,0,-8,-13,10,-5])
      case _:
                  print("Invalid input: ")
            
axes[0].plot(x,y)
axes[0].set_title('Sample Line Plot') 
axes[0].set_xlabel('Time-axis')  
axes[0].set_ylabel('Position-axis') 
axes[0].grid(True)
axes[1].plot(x,v)
axes[1].set_title('Velocity graph')
axes[1].set_xlabel('Time-axis')
axes[1].set_ylabel('Velocity-axis')
axes[1].grid(True)
axes[2].plot(x,a)
axes[2].set_title('Acceleration graph')
axes[2].set_xlabel('Time-axis')
axes[2].set_ylabel('Acceleration axis')
axes[2].grid(True)
plt.tight_layout()
plt.show()
