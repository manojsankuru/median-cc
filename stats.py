def median(xs: list[float]) -> float:
    """Return the median of xs.

    For an odd-length list, return the middle value of the sorted list.
    For an even-length list, return the mean of the two middle values.

    Raises:
        ValueError: If xs is empty.
    """
    if not xs:
        raise ValueError("median() of empty list")
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
