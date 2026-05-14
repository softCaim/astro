A = [[float(input("a_11: ")), float(input("a_12: "))],
     [float(input("a_21: ")), float(input("a_22: "))]]

B = [float(input("b_1: ")), float(input("b_2: "))]

def determinant(A, B):

    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return det

    det_1 = B[0] * A[1][1] - A[0][1] * B[1]
    det_2 = A[0][0] * B[1] - B[0] * A[1][0]
    return det_1, det_2

print(determinant(A, B))
