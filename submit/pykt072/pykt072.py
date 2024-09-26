def rotate_string(s):
    return s[1:] + s[0]

def generate_rotations(s):
    rotations = [s]
    for _ in range(1, len(s)):
        s = rotate_string(s)
        rotations.append(s)
    return rotations

def min_rotations_to_match(strings):
    n = len(strings)
    length = len(strings[0])
    min_steps = float('inf')

    # Generate all rotations for the first string
    first_string_rotations = generate_rotations(strings[0])

    for target in first_string_rotations:
        total_steps = 0
        for s in strings:
            found = False
            for steps in range(length):
                if s == target:
                    total_steps += steps
                    found = True
                    break
                s = rotate_string(s)
            if not found:
                return "NO"
        min_steps = min(min_steps, total_steps)

    return min_steps

def main():
    results = []
    while True:
        try:
            n = int(input().strip())
            if n == -1:
                break
            strings = []
            for _ in range(n):
                strings.append(input().strip())
            result = min_rotations_to_match(strings)
            results.append(result)
        except:
            break
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()