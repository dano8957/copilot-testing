def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be a positive integer greater than 0")
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True