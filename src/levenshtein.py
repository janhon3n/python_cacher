from Cacher import Cacher

def levenshtein(A, B):
    align_penalty = 1
    miss_align_penalty = 1

    if not len(A) or not len(B):
        return 0

    align = levenshtein(A[:-1], B[:-1]) + (0 if A[-1] == B[-1] else align_penalty)
    miss_align_A = levenshtein(A[:-1], B) + miss_align_penalty
    miss_align_B = levenshtein(A, B[:-1]) + miss_align_penalty

    return min(align, miss_align_A, miss_align_B)

levenshtein = Cacher(levenshtein)

print(levenshtein('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))