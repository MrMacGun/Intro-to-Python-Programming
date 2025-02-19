#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/20

def matrix_multiply():
    # Read input for matrix A (1xN)
    A = list(map(int, input().split()))
    
    # Read input for matrix B (NxN)
    N = len(A)
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split())))
    
    # Calculate the resulting matrix C (1xN)
    C = []
    for i in range(N):
        sum_product = 0
        for j in range(N):
            sum_product += A[j] * B[j][i]
        C.append(sum_product)
    
    # Output the result without trailing space
    print(*C, " ")

# Call the function
matrix_multiply()

