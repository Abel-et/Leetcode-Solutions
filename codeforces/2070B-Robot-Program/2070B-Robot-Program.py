# Convert to movement array
    moves = [ -1 if c == 'L' else 1 for c in s ]

    prefix = [0] * n
    prefix[0] = moves[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + moves[i]

    # Phase 1: first reach zero
    first_hit = -1
    for i in range(n):
        if x + prefix[i] == 0:
            first_hit = i + 1
            break

    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    # Phase 2: cycle from zero
    cycle = -1
    for i in range(n):
        if prefix[i] == 0:
            cycle = i + 1
            break

    if cycle == -1:
        print(1)
    else:
        print(1 + (k - first_hit) // cycle)