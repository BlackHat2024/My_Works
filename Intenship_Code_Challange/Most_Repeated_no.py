def frequency(arr):
    n = len(arr) 
    res = 0
    count = 1
     
    for i in range(1, n):
        if (arr[i] == arr[res]):
            count += 1
        else:
            count -= 1
         
        if (count == 0):
            res = i
            count = 1   
    return arr[res]
 
def main():
    array = [int(x) for x in input().split()] 
    most_frequency = frequency(array)
    print("The most repeated number is:", most_frequency)
    

if __name__== "__main__" :
    main()
