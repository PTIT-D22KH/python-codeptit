from itertools import combinations

def is_non_decreasing(subseq):
    """Check if a subsequence is non-decreasing."""
    return all(subseq[i] <= subseq[i + 1] for i in range(len(subseq) - 1))

def find_min_removals(arr):
    """Find the minimum number of elements to remove to make the array non-decreasing."""
    n = len(arr)
    max_length = 0
    subsequences = []
    all_results = []
    # Generate all possible subsequences
    for length in range(1, n + 1):
        for indices in combinations(range(n), length):
            subseq = [arr[i] for i in indices]
            
            if is_non_decreasing(subseq):
                if length > max_length:
                    max_length = length
                    subsequences = [subseq]
                    all_results.append(subseq)
                elif length == max_length:
                    subsequences.append(subseq)
                    all_results.append(subseq)
    
    k = n - max_length
    return k, subsequences, all_results

def format_number(num):
    """Format the number to print as integer if it is a whole number."""
    if num.is_integer():
        return int(num)
    return num

def main():
    n = int(input())
    arr = [float(i) for i in input().split()]
    
    k, subsequences, all_results = find_min_removals(arr)
    
    print(f"Total number of ways: {len(all_results)}")
    for result in all_results:
        formatted_result = [format_number(num) for num in result]
        print(formatted_result)
    print(f"Minimum K = {k}")
    for subsequence in subsequences:
        formatted_subsequence = [format_number(num) for num in subsequence]
        print(formatted_subsequence)

if __name__ == "__main__":
    main()