# python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range (n, -1, -1):
        j = i
        while True:
            l = (j * 2) + 1
            if l >= n:
                break
            if l+1 < n and data[l+l] < data[l]:
                l = l+1
            if data[j] > data[l]:
                swaps.append((j, l))
                data[j], data[l] = data[l], data[j]
                j = l
            else:
                break
    return swaps

def main():
    text = input("I or F: ")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    
    elif "F" in text:
        f = input()
        file = "tests/" + f
        with open(file, 'r') as x:
            n = int(x.readline())
            data = list(map(int,x.readline().split()))
       
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return    
       
if __name__ == "__main__":
    main()
