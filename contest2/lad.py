def converter(S, mapping):
    return int(''.join(mapping[ch] for ch in S))

def cerocero(S1, S2, S3, mapping):
    return not (mapping[S1[0]] == '0' or mapping[S2[0]] == '0' or mapping[S3[0]] == '0')

def solu(index, chars, mapping, used_digits, S1, S2, S3):
    if index == len(chars):
        if cerocero(S1, S2, S3, mapping):
            N1 = converter(S1, mapping)
            N2 = converter(S2, mapping)
            N3 = converter(S3, mapping)
            if N1 + N2 == N3:
                return f"{N1}\n{N2}\n{N3}"
        return None

    current_char = chars[index]
    for digit in range(10):
        if not used_digits[digit]:
            mapping[current_char] = str(digit)
            used_digits[digit] = True
            result = solu(index + 1, chars, mapping, used_digits, S1, S2, S3)
            if result:
                return result
            used_digits[digit] = False
            del mapping[current_char]

    return None

def solve(S1, S2, S3):
    chars = list(set(S1 + S2 + S3))
    
    if len(chars) > 10:
        return "UNSOLVABLE"
    
    mapping = {}
    used_digits = [False] * 10
    
    result = solu(0, chars, mapping, used_digits, S1, S2, S3)
    if result:
        return result
    return "UNSOLVABLE"

S1 = input().strip()
S2 = input().strip()
S3 = input().strip()

print(solve(S1, S2, S3))
