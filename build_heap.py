# python3
from array import array

def build_heap(a):
    n = len(a)
    swaps = [[0,0]]
    swaps.pop([0][0])
    k=-1
    i=0
    check = False

    while(True):
        if check==True and k==1:
            break
        if i == (n-1)/2:
            check = True
        if check ==True:
            k=k-2
        else:
            k=k+2
        
        if a[n-k]>a[n-(k+1)]:
            if (k+3)>n:
                if a[n-(k+1)]<a[n-(k+2)]:
                    swaps.append([n-(k+2), n-(k+1)])
                    a[n-(k+1)], a[n-(k+2)] = a[n-(k+2)], a[n-(k+1)] 
            else:  
                if a[n-(k+1)]<a[n-(k+3)]:
                    swaps.append([n-(k+3), n-(k+1)])
                    a[n-(k+1)], a[n-(k+3)] = a[n-(k+3)], a[n-(k+1)]

        else:
            if (k+3)>n:
                if a[n-k]<a[n-(k+2)]:
                    swaps.append([n-(k+2), n-k])
                    a[n-k], a[n-(k+2)] = a[n-(k+2)], a[n-k] 
            else:  
                if a[n-k]<a[n-(k+3)]:
                    swaps.append([n-(k+3), n-k])
                    a[n-k], a[n-(k+3)] = a[n-(k+3)], a[n-k]

        i=i+1
    
    


    return swaps


def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        data = input()
    elif "F" in text:
        text2 = input()
        if "a" in text2:
            return()
        with open ("test/"+text2, encoding="utf-8") as fails:
            n = int (fails.readline())
            data = fails.readline()
            
    else:
        return()


    
    data = list(map(int, data.split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
