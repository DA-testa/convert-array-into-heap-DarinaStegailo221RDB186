# python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range (n, -1, -1):
        j = i
        while True:
            z = (j*2)+1
            if z >= n:
                break
            if z+1 < n and data[z+1] < data[z]:
                z = z+1
            if data[j] > data[z]:
                swaps.append((j, z))
                data[j], data[z] = data[z], data[j]
                j = z
            else:
                break
    return swaps

def main():
    text = input("I or F: ")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in text:
        f = input()
        file = './tests/' + f
            with open(file, 'r', encoding='utf-8') as x:
                n = int(x.readline())
                data = list(map(int, x.readline().split()))
    else:
        print("Error")
        return 
    
    assert data is not None and len(data) == n
    swaps = build_heap(data)
    assert len(swaps) <= n*4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
       
if __name__ == "__main__":
    main()
