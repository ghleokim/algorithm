def count(compressed, n_count, next_n):
    n_str = str(n_count) if n_count > 1 else ''
    return f"{compressed}{n_str}{next_n}"

def compress(n, compressed, leftover):
    if len(leftover) < n:
        return len(leftover) + len(compressed)
    else:
        n_count = 1
        next_n = leftover[:n]
        leftover = leftover[n:]

        while True:
            if len(leftover) < n:
                compressed = count(compressed, n_count, next_n)
                return compress(n, compressed, leftover)

            if next_n == leftover[:n]:
                n_count += 1
                leftover = leftover[n:]
            else:
                compressed = count(compressed, n_count, next_n)
                return compress(n, compressed, leftover)



def solution(s):
    min_length = 1001

    if len(s) == 1: return 1

    for n in range(1, len(s)):
        min_length = min(compress(n, '', s), min_length)

    return min_length
