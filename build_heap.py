# python3

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        while(True):
            min_index = i
            a = 2*i + 1
            if a < n and data[a] < data[min_index]:
                min_index = a
            b = 2*i + 2
            if b < n and data[b] < data[min_index]:
                min_index = b
            if i != min_index:
                swaps.append((i, min_index))
                data[i], data[min_index] = data[min_index], data[i]
                i = min_index
                continue
            break
    return swaps


def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        text2 = input()
        if "a" in text2:
            return()
        with open ("tests/"+text2, encoding="utf-8") as fails:
            n = int (fails.readline())
            data = list(map(int, fails.readline().split()))
            
    else:
        return()
    
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()