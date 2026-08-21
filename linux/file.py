def merge_sort(arr):
    """
    Sort an array using merge sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: First sorted list
        right: Second sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    print("Sorted array:", merge_sort(arr))
    print("Testing branch move from main")
    