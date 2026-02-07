### Using parametric equations to generate surfaces.
### Equations for a torus:
### x(u, v) = (R + r * cos(v)) * cos(u)
### y(u, v) = (R + r * cos(v)) * sin(u)
### z(u, v) = r * sin(v)
### where u, v \in [0, 2 * \pi]

import numpy as np 


def torus(R=2.0, r=1.0, u_res=40, v_res=20):
    """Parametric equations for torus to generate mesh"""
    
