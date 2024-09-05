import numpy as np


def display_vector(vector, name):
    variables = ["i", "j", "k"]
    output = f"Vektori {name} = "
    for i in range(len(vector)):
        output += f"{vector[i]}{variables[i]} "

    print(output)


# teht 1 - 20-alkioinen taulukko
array = np.random.randint(20, size=20)
array.sort()
array = array[::-1]
array = array.reshape(4, 5)
print("<-------- Kaksiulotteinen taulukko -------->")
print(array)

# teht 2 - vektorit
vector_u = np.array([2, 3])
vector_v = np.array([4, -7])
vector_uu = np.array([1, 1, 1])
vector_vv = np.array([3, -3, 2])

print("<-------- Numpy vektorit -------->")
display_vector(vector_u,"U")
display_vector(vector_v,"V")
display_vector(vector_uu,"UU")
display_vector(vector_vv,"VV")

# teht 3 - vektorien normi
norm_u = np.linalg.norm(vector_u)
norm_v = np.linalg.norm(vector_v)
norm_uu = np.linalg.norm(vector_uu)
norm_vv = np.linalg.norm(vector_vv)

print("<-------- Vektorien normit -------->")
print(f"U normi: {norm_u}")
print(f"V normi: {norm_v}")
print(f"UU normi: {norm_uu}")
print(f"VV normi: {norm_vv}")
