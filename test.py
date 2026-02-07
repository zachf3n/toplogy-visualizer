# Create parameter grid
import numpy as np
R = 2.0
r = 1.0
u_res = 40
v_res = 20
u = np.linspace(0, 2 * np.pi, u_res, endpoint=False) # step size changes when False
v = np.linspace(0, 2 * np.pi, v_res, endpoint=False)
print(f"u = {u}")
print(f"v = {v}")

u, v = np.meshgrid(u, v)
print(f"u_mesh = {u}")
print(f"v_mesh = {v}")

# parametric equations. 
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")


