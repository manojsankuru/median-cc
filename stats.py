def median(xs: list[float]) -> float:
    if not xs:
        raise ValueError("median() of empty list")
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
