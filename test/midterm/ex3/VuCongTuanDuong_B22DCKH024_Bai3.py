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
    #dp[n][v] la so chuoi co chieu dai n ket thuc voi nguyen am v

    # so chuoi co chieu dai 1 la nguyen am thi chi co duy nhat 1
    for v in vowels:
        dp[v][1] = 1


    for n in range(2, N + 1):
        for v in vowels:
            dp[v][n] = 0
            for prev_v in transitions[v]:
                dp[v][n] += dp[prev_v][n - 1]


    result = 0
    for v in vowels:
        result += dp[v][N]

    return result


N = int(input())
print(f"So chuoi duoc tao nen tu luat tren ma co chieu dai {N}: {count_vowel_permutations(N)}")