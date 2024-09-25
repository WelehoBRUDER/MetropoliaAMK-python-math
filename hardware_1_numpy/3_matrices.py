import numpy as np


def multiply_matrices(a, b):  # void
    try:
        print(f"V: {np.dot(a, b)}")
    except Exception:
        print("V: Ei määritetty!")


simple_matrices = {
    "1.": {
        "A": [[[-1, 2], [3, 1]], [[0, 1, 3], [2, -3, 5]]],
        "B": [[[1, 3, 5], [0, -2, 1], [2, -1, 4]], [[1], [-3], [-1]]],
        "C": [[[2, 0, 1], [1, -3, 4], [0, 1, 5]], [[3], [-5], [7]]],
        "D": [[[1, -4, 2], [3, 0, -2], [2, 1, 0]], [[5, 1, -1], [-2, 1, 3], [0, 3, 4]]]
    },
    "2.": {
        "mats": [[[1, 2, 3], [1, 0, -2]], [[1], [4], [2]], [[1, 0, 2]]],
        "calcs": [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]]  # AB, BA, etc...
    },
    "3.": {
        "mats": [[[1, 0.5], [2, 1]], [[-1, -2], [2, 4]]],
        "calcs": [[0, 1], [1, 0]]
    }
}

for task in simple_matrices:
    print("-" * 12)
    print(f"Tehtävä {task}")
    print("-" * 12)
    if task == "1.":
        for part in simple_matrices[task]:
            print(f"{part})")
            matrices = simple_matrices[task][part]
            a = np.array(matrices[0])
            b = np.array(matrices[1])
            multiply_matrices(a, b)
    else:
        mats = []
        keys = ["A", "B", "C"]
        for mat in simple_matrices[task]["mats"]:
            mats.append(np.array(mat))
        for calc in simple_matrices[task]["calcs"]:
            print(f"{keys[calc[0]]}{keys[calc[1]]}")
            multiply_matrices(mats[calc[0]], mats[calc[1]])



