# python3

def build_heap(data):
    swaps = []
    n = len(data)
    # Taisu ciklu pa vecāku mezgliem koka indeksu sarakstā (sākot no apakšas)
    for i in range(n//2, -1, -1):
        # Turpina mainīt elementus, līdz koka īpašība ir apmierinoša
        while(True):
            # Inicializē minimālā elementa indeksu
            min_index = i
            # Aprēķina kreisās un labās bērna mezglu indeksus
            a = 2*i + 1
            b = 2*i + 2
            # Jāizvēlās kreiso vai labo bērnu
            # Pārbauda, vai kreisais bērna mezgls ir mazāks par pašreizējo elementu
            if a < n and data[a] < data[min_index]:
                # Ja ir, minimālā elementa indekss = kreisā bērna indekss
                min_index = a
            # Tas pats ar labo
            if b < n and data[b] < data[min_index]:
                min_index = b
            # Ja minimālais indekss pamainījās, apmaina elementus (swap)
            if i != min_index:
                # Pievieno sarakstam tos elementus kurus mainām
                swaps.append((i, min_index))
                # Apmaina elementus skrakstā "data"
                data[i], data[min_index] = data[min_index], data[i]
                # Atjauno indeksu
                i = min_index
                # Turpinā 
                continue
            # Ja minimālā elementa indekss nav izmainīts, iziet no cikla
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
    
    # Pārbauda, vai saraksta "data" garums ir vienāds ar n
    assert len(data) == n

    swaps = build_heap(data)
    # Izvada swaps skaitu
    print(len(swaps))
    # Izvada swaps 
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()