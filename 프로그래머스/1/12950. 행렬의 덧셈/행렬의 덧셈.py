# def solution(arr1, arr2):
#     row = len(arr1)
#     col = len(arr1[0])
#     answer = [[0 for _ in range(col)] for _ in range(row)]
    
#     for i in range(row):
#         for j in range(col):
#             answer[i][j] = arr1[i][j] + arr2[i][j]
#     return answer

import numpy as np

def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    
    answer = a + b
    return answer.tolist() #ndarray -> list
    