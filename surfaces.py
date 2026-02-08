### Using parametric equations to generate surfaces.
### Equations for a torus:
### x(u, v) = (R + r * cos(v)) * cos(u)
### y(u, v) = (R + r * cos(v)) * sin(u)
### z(u, v) = r * sin(v)
### where u, v \in [0, 2 * \pi]
### u is the azimuthal angle (angle around the z-axis)
### v is the poloidal angle (angle around the tube of the torus)

import numpy as np 


def torus(R=2.0, r=1.0, u_res=40, v_res=20):
     # sourcery skip: merge-list-appends-into-extend, use-itertools-product
     """
     Generate a torus mesh.
    
    Parameters:
    -----------
    R : float
        Major radius (distance from center to tube center)
    r : float
        Minor radius (tube radius)
    u_res : int
        Resolution in u direction (around major circle)
    v_res : int
        Resolution in v direction (around minor circle)
    
    Returns:
    --------
    vertices : ndarray, shape (n, 3)
        Vertex positions
    faces : ndarray, shape (m, 3)
        Triangle faces as vertex indices
    """
     # Create parameter grid
     u = np.linspace(0, 2 * np.pi, u_res, endpoint=False) # step size changes when False
     v = np.linspace(0, 2 * np.pi, v_res, endpoint=False)

     u, v = np.meshgrid(u, v)
    
     # parametric equations. 
     x = (R + r * np.cos(v)) * np.cos(u)
     y = (R + r * np.cos(v)) * np.sin(u)
     z = r * np.sin(v)

     # flatten and stack in to vertices.
     vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)

     # generate faces
     faces = []
     for i in range(v_res):
          for j in range(u_res):
               # current vertex index 
               v1 = i * u_res + j
               # next in the u direction
               v2 = i * u_res + (j+1) % u_res
               #next in the v direction
               v3 = ((i+1) % v_res) * u_res + j
               v4 = ((i+1) % v_res) * u_res + (j+1) % u_res

               # two triangles per quad
               faces.append([v1, v2, v3])
               faces.append([v2, v4, v3])

     faces = np.array(faces)

     return vertices, faces