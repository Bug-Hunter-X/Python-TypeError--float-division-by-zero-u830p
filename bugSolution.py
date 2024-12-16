def my_function(x):
    if abs(x) < 1e-9:  # Check for near-zero values
        return 0
    else:
        return 1 / x