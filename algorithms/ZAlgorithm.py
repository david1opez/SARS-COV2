def find(text, pattern):
    # Concatenate pattern, a unique delimiter, and text
    concat = pattern + '$' + text
    z = [0] * len(concat)

    # Z-algorithm to fill z array
    def calculate_z(concat):
        n = len(concat)
        left, right, k = 0, 0, 0
        for i in range(1, n):
            if i > right:
                left, right = i, i
                while right < n and concat[right] == concat[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1
            else:
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]
                else:
                    left = i
                    while right < n and concat[right] == concat[right - left]:
                        right += 1
                    z[i] = right - left
                    right -= 1

    calculate_z(concat)

    # Collect indices where pattern matches text
    indices = []
    pattern_len = len(pattern)
    for i in range(pattern_len + 1, len(concat)):
        if z[i] == pattern_len:
            indices.append(i - pattern_len - 1)

    return indices