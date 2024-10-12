from itertools import combinations

def is_non_decreasing(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))


def solve(arr):
    n = len(arr)
    max_length = 0
    subsequences = []
    all_results = []

    for length in range(1, n + 1):
        for index in combinations(range(n), length):
            b = [arr[i] for i in index]
            if is_non_decreasing(b):
                if length > max_length:
                    max_length = length
                    subsequences = [b]
                    all_results.append(b)
                elif length == max_length:
                    subsequences.append(b)
                    all_results.append(b)
    
    k = n - max_length
    return k, subsequences, all_results

def format_number(num):
    if num.is_integer():
        return int(num)
    return num

def main():
    n = int(input())
    arr = [float(i) for i in input().split()]
    
    k, subsequences, all_results = solve(arr)
    
    print(f"Total number of ways: {len(all_results)}")
    for result in all_results:
        temp = [format_number(num) for num in result]
        print(temp)
    print(f"Minimum K = {k}")
    for subsequence in subsequences:
        temp = [format_number(num) for num in subsequence]
        print(temp)

if __name__ == "__main__":
    main()