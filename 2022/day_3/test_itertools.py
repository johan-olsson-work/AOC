import itertools
for a, b in itertools.combinations(test_data, 2):
    #c = compare(a, b)
    print(f"a: {a}")
    print(f"b: {b}")
    for c in a:
        if c in b:
            print(f"Found matching {c} IN {a} AND {b}")
