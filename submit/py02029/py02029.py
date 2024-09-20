def cmp(item):
    # Sort primarily by frequency (descending), then by value (ascending)
    return (-item[1], item[0])

def main():
    # Read input
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    
    # Count the frequency of each element
    d = {}
    s = 0
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
        s = max(s, d[x])
    
    
    
    # Sort the dictionary items by custom key
    sorted_items = sorted(d.items(), key=cmp)
    
    # Print the sorted result
    for item in sorted_items:
        print(f"{item[0]}: {item[1]}")

if __name__ == '__main__':
    main()