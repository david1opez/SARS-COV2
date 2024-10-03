def find(text, pattern):
    def build_bad_char_table(pattern):
        bad_char_table = [-1] * 256
        for i in range(len(pattern)):
            bad_char_table[ord(pattern[i])] = i
        return bad_char_table

    m = len(pattern)
    n = len(text)

    bad_char_table = build_bad_char_table(pattern)
    
    indices = []
    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            indices.append(s)
            s += (m - bad_char_table[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char_table[ord(text[s + j])])

    return indices

