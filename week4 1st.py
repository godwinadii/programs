import numpy as np
import tensorflow as tf

s = 50
m = np.array([[0, 2], [2, 3]])
v = np.array([[0, 2]])
print(f"Scalar: {s}\n\nMatrix:\n{m}\n\nVector:\n{v}")

print("\nTensor - Numeric:\n", tf.fill([3, 3], 4).numpy())
print("\nTensor - String:\n", tf.fill([2, 2], "str").numpy())

w, eig_v = np.linalg.eig(m)
print("\nEigenvalues:\n", w)
print("\nEigenvectors:\n", eig_v)
print("\nMatrix norm:", np.linalg.norm(m))
