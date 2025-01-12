import numpy as np

def compute_cross_product(array1, array2):
    
    array1 = np.array(array1)
    array2 = np.array(array2)
   
    return np.cross(array1, array2)

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = compute_cross_product(a, b)
    print("Cross Product:", result)

