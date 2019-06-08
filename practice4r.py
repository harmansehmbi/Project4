S1 = {1, 2, 3, 'a', 'b'}
S2 = {1, 'a', 'b'}

print(S2.issubset(S1))
print()
print(S1.issuperset(S2))
print()
print(S1.union(S2))
print()
print(S1.intersection(S2))
print()
print(S1.difference(S2))
print()
print(S1.symmetric_difference(S2))