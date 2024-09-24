def can_find_subarray_with_average_geq(mid, A, N):
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1] - mid
    
    min_prefix_sum = 0
    for i in range(1, N + 1):
        if prefix_sum[i] - min_prefix_sum >= 0:
            return True
        if i >= 1:
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])
    
    return False

def find_max_average_length(N, A):
    left, right = min(A), max(A)
    precision = 1e-5
    while right - left > precision:
        mid = (left + right) / 2
        if can_find_subarray_with_average_geq(mid, A, N):
            left = mid
        else:
            right = mid
    
    max_average = left
    
    # Find the longest subarray with the maximum average
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1] - max_average
    
    min_prefix_sum = 0
    max_length = 0
    start_index = 0
    for i in range(1, N + 1):
        if prefix_sum[i] - min_prefix_sum >= 0:
            max_length = max(max_length, i - start_index)
        if i >= 1:
            if prefix_sum[i] < min_prefix_sum:
                min_prefix_sum = prefix_sum[i]
                start_index = i
    
    return max_length

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    
    result = find_max_average_length(N, A)
    print(result)

if __name__ == '__main__':
    main()