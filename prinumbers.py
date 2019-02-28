#Program for printing prime numbers in one line
[p for p in range(2,101) if 0 not in [p%d for d in range(2,p)] ]
