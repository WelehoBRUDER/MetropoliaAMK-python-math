import numpy as np

# teht 1 - 20-alkioinen taulukko
array = np.random.randint(20, size=20)
array.sort()
array = array[::-1]
array = array.reshape(4, 5)
print(array)

# teht 2 - vektorit
vector_u = np.array([2, 3])
vector_v = np.array([4, -7])
vector_uu = np.array([1, 1, 1])
vector_vv = np.array([3, -3, 2])

print(f"U = {vector_u}")
print(f"V = {vector_v}")
print(f"UU = {vector_uu}")
print(f"VV = {vector_vv}")

# teht 3 - vektorien normi
norm_u = np.linalg.norm(vector_u)
norm_v = np.linalg.norm(vector_v)
norm_uu = np.linalg.norm(vector_uu)
norm_vv = np.linalg.norm(vector_vv)

print(f"U normi: {norm_u}")
print(f"V normi: {norm_v}")
print(f"UU normi: {norm_uu}")
print(f"VV normi: {norm_vv}")