import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from fractions import Fraction
x= []
y= []
v= []
a= []
fig,axes=plt.subplots(3,1, figsize=(12,7))
xi=float(Fraction(input("Input initial position: ")))
vi=float(Fraction(input("Input initial velocity: ")))
ai=-9.8
Θ_deg=float(Fraction(input("Input angle: ")))
Θ=np.deg2rad(Θ_deg)
t=sp.symbols('t')

xd= vi*sp.cos(Θ)*t
yd=xi+vi*sp.sin(Θ)*t-(1/2)*(-ai)*t**2
solution=sp.solve(yd,t)
real_solutions = [sol for sol in solution if sol.is_real and sol >= 0]

# Select the first real positive solution (time of flight)
if real_solutions:
    time_of_flight = real_solutions[0]
    print(time_of_flight)
else:
    raise ValueError("No valid real solution for time of flight")

time_step=np.linspace(0,time_of_flight,1000)
tmax=time_of_flight/2
ymax=yd.evalf(subs={t:tmax})
xmax=xd.evalf(subs={t:time_of_flight})
for i in time_step:
 
    
   
    Vx= sp.diff(xd,t)
    Vy= sp.diff(yd,t)
    ax= sp.diff(Vx,t)
    ay= sp.diff(Vy,t)
    ti=i
    xd_val=xd.evalf(subs={t:ti})
    yd_val=yd.evalf(subs={t:ti})
    Vx_val=Vx.evalf(subs={t:ti})
    Vy_val=Vy.evalf(subs={t:ti})
    impact_velocity=sp.sqrt(Vx_val**2+Vy_val**2)
    x.append(xd_val)
    y.append(yd_val)
    v.append(sp.sqrt(Vx_val**2+Vy_val**2))
    a.append(ai)

axes[0].plot(x, y, label='Trajectory', color='blue')
axes[0].set_title("Projectile Trajectory")
axes[0].set_xlabel("Horizontal Distance (m)")
axes[0].set_ylabel("Vertical Height (m)")
axes[0].legend()

# Plot velocity vs time
axes[1].plot(time_step, v, label='Velocity (Speed)', color='red')
axes[1].set_title("Velocity vs. Time")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Speed (m/s)")
axes[1].legend()

# Plot acceleration vs time
axes[2].plot(time_step, a, label='Vertical Acceleration', color='green')
axes[2].set_title("Acceleration vs. Time")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration (m/s^2)")
axes[2].legend()
plt.subplots_adjust(bottom=0.5)
info_text=f"""
Maximum hieght: {ymax:.2f} m
Maximum distance: {xmax:.2f} m
Impact velocity: {impact_velocity:.2f} m"""
fig.text(0.1, 0.02, info_text, fontsize=10, color="black", 
         bbox=dict(facecolor="white", alpha=0.7, boxstyle="round"))

plt.tight_layout()
plt.show()