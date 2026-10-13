def process(values):
    total = 0
    for v in values:
        if v % 2 == 0:
            if v > 10:
                total += v
            else:
                total -= v
        else:
            total += 1
    return total