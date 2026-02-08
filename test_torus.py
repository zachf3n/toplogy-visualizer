from surfaces import torus
from export import write_obj

# generate torus
vertices, faces = torus(R=2, r=1, u_res=40, v_res=20)

# Print some info
print(f"Generated torus with {len(vertices)} vertices and {len(faces)} faces.")
print(f"\nFirst 5 vertices:")
for i in range(5):
    print(f"    v{i}: {vertices[i]}")

print(f"\nFirst 5 faces:")
for i in range(5):
    print(f"    f{i}: {faces[i]}")

write_obj("examples/torus.obj", vertices=vertices, faces=faces)
