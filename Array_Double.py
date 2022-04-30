
def modifyList(array):
    arr= [array[0]*2]
    for i in range (1 , len(array)-1) : 
        if(array[i-1]==array[i+1]):
            array[i] =0 ; 
            arr.insert(0, array[i])
        else:
            if (array[i]==0) :
                arr.insert(0, array[i])
            else :
                arr.append(array[i]*2) ; 

      
    
    if(array[len(array)-1]==0) :
        arr.insert(0, 0)
    
    else:
        arr.append(array[len(array)-1]*2)

    return arr 


def main():
    array = [int(x) for x in input().split()] 
    array = modifyList(array)
    print(*array) 


if __name__== "__main__" :
    main()
