def power_set(S):
    S = list(S)
    n = len(S)

    def generate_subsets(index):
        if index == n:
            return [set()] 
        subsets_without_element = generate_subsets((index + 1))
        subsets_with_element = []
        for subset in subsets_without_element:
            new_subset = subset.copy()
            new_subset.add(S[index])
            subsets_with_element.append(new_subset)
        return (subsets_without_element + subsets_with_element)
    return (generate_subsets(0))

A = [1,2,3,4]
B = [3,4,5,6]

A = set(A)
B = set(B)

print("Set A:", A)
print("Set B:", B,"\n")

print("Union (A U B):", A.union(B))
print("Intersection (A n B):", A.intersection(B))
print("Difference (A - B):", A.difference(B))
print("Difference (B - A):", B.difference(A))
print("Symmetric Difference (B /\ A):", A.symmetric_difference(B),"\n")

print("Is A a subset of B:", A.issubset(B))
print("Is B a subset of A:", B.issubset(A))

print(power_set({1,2,3}))