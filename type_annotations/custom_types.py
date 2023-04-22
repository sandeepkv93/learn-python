from typing import List

Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2.0, [1.0, -4.2, 5.4])

print(new_vector)  # [2.0, -8.4, 10.8]

Vectors = List[Vector]

matrix: Vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def merge_vectors(vectors: Vectors) -> Vector:
    return [sum(elements) for elements in zip(*vectors)]


vector1: Vector = [1, 2, 3]
vector2: Vector = [4, 5, 6]
vector3: Vector = [7, 8, 9]

merged_vector: Vector = merge_vectors([vector1, vector2, vector3])
print(merged_vector)  # [12, 15, 18]
