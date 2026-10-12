def compound_interest(p: float, r: float, n: int, t: int) -> float:
    """
    Return accumulated amount using compound interest.
    p – principal, r – annual rate (e.g., 0.05), n – # compounds per year,
    t – total years.
    """
    return p * (1 + r / n) ** (n * t)

