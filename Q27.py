class Vector:
    def __init__(self, components):
        self._components = list(components)

    def __str__(self):
        return f"{len(self._components)}-dimensional vector: {self._components}"

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply by scalar")
        return Vector([x * scalar for x in self._components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of same dimension")
        return Vector([a + b for a, b in zip(self._components, other._components)])

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of same dimension")
        return Vector([a - b for a, b in zip(self._components, other._components)])

    def __matmul__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of same dimension")
        return sum(a * b for a, b in zip(self._components, other._components))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1)
print(2 * v1)
print(v1 * 3)
print(v1 + v2)
print(v1 - v2)
print(v1 @ v2)

try:
    print(v1 + Vector([1, 2]))
except ValueError as e:
    print(e)