
def findLargestSquare(arr, m, n, maxsize, x, y ):

    if m < 0 or n < 0:
        return 0, maxsize, x, y
    #For each point check recursively if contain horizontaly, verticaly and diagonaly only ones and increase size
    #Otherwise if 0 cell is found reset size to 0
    left, maxsize, x, y = findLargestSquare(arr, m, n - 1, maxsize ,x , y )
    top, maxsize , x, y = findLargestSquare(arr, m - 1, n, maxsize, x, y)
    diagonal, maxsize, x, y  = findLargestSquare(arr, m - 1, n - 1, maxsize, x ,y)
   
    size = 1 + min(min(top, left), diagonal) if arr[m][n] else 0
    if(size> maxsize) :
        x, y = m ,n
    
    return size, max(maxsize, size) , x, y 
 
 
def findLargestSquareSubmatrix(arr) -> int:
 
    if not arr or not len(arr):
        return 0
 
    (M, N) = (len(arr), len(arr[0]))
    x, y = M-1 , N-1
    maxsize,x,y = findLargestSquare(arr, M - 1, N - 1, 0 , x , y)[1:4]
   
    return maxsize, x, y 
 
 
if __name__ == '__main__':
    arr = [
        [0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 1, 0]
       
    ]
    size, x4, y4 = findLargestSquareSubmatrix(arr)
    
    x1 , y1 = x4+1-size , y4+1 - size
    x2 , y2 = x4 , y4+1 - size 
    x3 , y3 = x4+1-size , y4
    #size of submatrix
    print("The largest matrix with 1's has size:", size )
    #here we print all borders of sub array
    print("Cordinates are: ({0}, {1}), ({2}, {3}), ({4}, {5}), ({6}, {7})".format(x1, y1, x2, y2, x3, y3, x4, y4))
  

