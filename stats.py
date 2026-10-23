def median(xs: list[float]) -> float:
    s = sorted(xs)
    n = len(s)
    return s[n // 2]  # bug: wrong for even-length lists
