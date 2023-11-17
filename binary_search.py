def binarySearch(lists: list, item: int) -> int:
    low = 0
    high = len(lists) - 1
    while low <= high:
        mid = high + low
        guess = lists[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid -1
    return None