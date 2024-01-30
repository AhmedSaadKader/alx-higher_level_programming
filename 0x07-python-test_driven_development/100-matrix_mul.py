#!/usr/bin/python3
"""

"""


def matrix_mul(mul_a, mul_b):
	for i in range(len(mul_a)):
		row_a = mul_a[i]
		row_b = mul_b[i]
		for num in row_a:
			num_1 = row_a[0]
			num_2 = row_a[1]
		print(i)

if __name__ == "__main__":
	matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
