
def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result = []

    while left and right:
        if left[0] >= right[0]:
            