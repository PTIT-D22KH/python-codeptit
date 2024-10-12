def count_vowel_permutations(N):
    if N == 0:
        return 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    transitions = {
        'a': ['e'],
        'e': ['a', 'i'],
        'i': ['a', 'e', 'o', 'u'],
        'o': ['i', 'u'],
        'u': ['a']
    }

    dp = {v: [0] * (N + 1) for v in vowels}

    # Initialize for strings of length 1
    for v in vowels:
        dp[v][1] = 1

    # Fill the dp table
    for n in range(2, N + 1):
        for v in vowels:
            dp[v][n] = sum(dp[prev_v][n - 1] for prev_v in transitions[v])

    # Sum up all the ways to form strings of length N
    result = sum(dp[v][N] for v in vowels)
    return result

# Example usage:
N = 5
print(f"Number of valid strings of length {N}: {count_vowel_permutations(N)}")